"""Keep spoken exports, edit cues, chapter handoffs and preserved sources reliable."""
import copy
import hashlib
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT/'tools'))
import filming_pack as film
import guided_course as course


class FilmingPack(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = course.catalog(ROOT)
        cls.by = {r['id']: r for r in cls.rows}
        cls.generated = course.outputs(ROOT)

    def test_every_teaching_task_has_anchored_overlays_and_a_handoff(self):
        stats = film.validate(self.rows, course.PRACTICAL_IDS)
        self.assertEqual(len(course.CORE_IDS), 25)
        self.assertEqual(len(course.ADV_IDS), 8)
        self.assertGreaterEqual(stats['teaching_overlays'], 33)
        self.assertEqual(stats['walkthrough_chapters'], 72)
        for lid in course.CORE_IDS + course.ADV_IDS:
            self.assertTrue(self.by[lid]['checkpoint'])
            self.assertEqual(self.generated[course.read_link(self.by[lid])].strip(), self.by[lid]['read'])

    def test_each_walkthrough_take_exports_only_its_complete_speech(self):
        manifest = json.loads(self.generated['COURSE-MANIFEST.json'])
        records = {r['id']: r for r in manifest['lessons']}
        for lid in course.PRACTICAL_IDS:
            scenes = film.chapters(self.by[lid]['text'])
            speech = '\n\n'.join(s['Narration'] for s in scenes)
            self.assertEqual(self.generated[f'teleprompter/walkthrough/{lid}.txt'].strip(), speech)
            self.assertEqual(records[lid]['spoken_sha256'], hashlib.sha256(speech.encode()).hexdigest())
            self.assertEqual(len(records[lid]['chapter_takes']), film.CHAPTER_COUNTS[lid])
            for scene in scenes:
                path = f"teleprompter/walkthrough/{lid}-{scene['number']:02d}.txt"
                self.assertEqual(self.generated[path].strip(), scene['Narration'])
                self.assertNotRegex(self.generated[path], r'\*\*(Show|Verify|Overlay|Capture dependency):')

    def test_stale_overlay_anchor_is_rejected(self):
        rows = copy.deepcopy(self.rows)
        row = rows[0]
        cue = film.overlays(row['text'])[0][0]
        row['text'] = row['text'].replace('| '+cue+' |', '| A line that is never spoken |', 1)
        with self.assertRaisesRegex(ValueError, 'Overlay cue'):
            film.validate(rows, course.PRACTICAL_IDS)

    def test_missing_or_repeated_chapter_is_rejected(self):
        for replacement in ['#### Removed chapter 2', '#### Chapter 1']:
            rows = copy.deepcopy(self.rows)
            row = next(r for r in rows if r['id'] == 'W01')
            row['text'] = row['text'].replace('#### Chapter 2', replacement, 1)
            with self.assertRaises(ValueError):
                film.validate(rows, course.PRACTICAL_IDS)

    def test_blank_or_placeholder_walkthrough_speech_is_rejected(self):
        for replacement in ['', '[INSERT SCRIPT]']:
            rows = copy.deepcopy(self.rows)
            row = next(r for r in rows if r['id'] == 'W01')
            scene = film.chapters(row['text'])[0]
            row['text'] = row['text'].replace(scene['Narration'], replacement, 1)
            with self.assertRaises(ValueError):
                film.validate(rows, course.PRACTICAL_IDS)

    def test_active_reserve_still_teaches_the_reviewed_calculation_and_shared_money(self):
        spoken = self.by['2.3']['read']
        for value in ['$7,200', '$43,200', '$32,000', '$11,200', '$500']:
            self.assertIn(value, spoken)
        self.assertIn('including required household debt payments', spoken)
        self.assertIn("We can't assign the same monthly surplus to both", spoken)
        self.assertIn('reduced-spending example', spoken)

    def test_original_and_revised_protected_scripts_reject_mutation(self):
        data = film.revision(ROOT)
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            paths = ['production/stepwise-revision.json', data['authority']]
            paths += [r['archive'] for r in data['preserved_originals']]
            paths += list(data['active_protected'])
            for path in paths:
                target = root/path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT/path, target)
            film.revision(root)
            for path in [r['archive'] for r in data['preserved_originals']] + list(data['active_protected']):
                target = root/path
                original = target.read_bytes()
                target.write_bytes(original+b'changed')
                with self.assertRaisesRegex(ValueError, 'changed'):
                    film.revision(root)
                target.write_bytes(original)
            film.revision(root)

    def test_reference_head_and_capture_status_do_not_claim_a_shipped_app(self):
        text = (ROOT/'V1-COURSE-ALIGNMENT.md').read_text(encoding='utf-8')
        self.assertIn(course.APP_SHA, text)
        self.assertIn('issuecomment-5618008737', text)
        self.assertIn('not an assertion', text)
        self.assertIn('Every row remains unverified', self.generated['WALKTHROUGH-CAPTURE-DEPENDENCIES.md'])
        self.assertEqual(hashlib.sha1(b'blob '+str(len((ROOT/'CAPTURE-RECEIPTS.md').read_bytes())).encode()+b'\0'+(ROOT/'CAPTURE-RECEIPTS.md').read_bytes()).hexdigest(), '3f2593d83d57f979070b0d1dae95a958671263af')


if __name__ == '__main__':
    unittest.main()

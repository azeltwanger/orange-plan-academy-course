#!/usr/bin/env python3
"""Narrow inventory-contract update for the explicitly authorized A7.2 merge."""
from pathlib import Path
import hashlib

p=Path('tests/test_member_deliverables.py');data=p.read_bytes()
assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()=='d2be90c617dfe350ce7601d77a236f38c8f217b4'
before="""    def test_existing_inventory_is_preserved(self):
        counts = json.loads(read('COURSE-MANIFEST.json'))['counts']
        self.assertEqual(counts, {'core':51, 'advanced':15, 'working_sessions':10, 'device_demos':1})"""
after="""    def test_inventory_and_authorized_custody_merge(self):
        manifest = json.loads(read('COURSE-MANIFEST.json'))
        self.assertEqual(manifest['counts'], {'core':51, 'advanced':14, 'working_sessions':10, 'device_demos':1})
        ids = {row['id'] for row in manifest['lessons']}
        self.assertEqual(len(ids), 76)
        self.assertNotIn('A7.2', ids)
        self.assertEqual(len(manifest['member_order']), 65)
        self.assertEqual(len(set(manifest['member_order'])), 65)
        merged = manifest['merged_lessons']
        self.assertEqual(len(merged), 1)
        self.assertEqual(merged[0]['id'], 'A7.2')
        self.assertEqual(merged[0]['source_commit'], 'f6392a6341c23c557e605506dab3530b67efa146')
        self.assertEqual(merged[0]['blob'], '0443c4640a4f4b431429eab204f5fe9dc0b67413')
        self.assertEqual(merged[0]['destinations'], ['7.1', '7.4', 'W07'])
        self.assertTrue(set(merged[0]['destinations']).issubset(ids))
        self.assertFalse((ROOT / merged[0]['path']).exists())"""
assert data.decode().count(before)==1
changed=data.decode().replace(before,after,1)
assert changed.replace(after,before,1)==data.decode()
p.write_text(changed)
p=Path('HANDOFF.md');s=p.read_text()
a='Original source-material, fixture, toolkit, tests, capture register and the original 264-file recovery inventory are unchanged.'
b='Original source-material, fixture, toolkit, capture register and the original 264-file recovery inventory are unchanged. The one inventory test now expects 14 situational lessons and verifies the exact authorized A7.2 merge and its destinations; all other member-material tests are unchanged.'
assert s.count(a)==1;p.write_text(s.replace(a,b,1))
p=Path('FINALIZATION-STATUS.md');s=p.read_text()
a='Original sources, fixture, toolkit, tests and capture records are preserved; exact implementation and verification evidence belongs in the PR handoff.'
b='Original sources, fixture, toolkit and capture records are preserved. The inventory test is updated specifically for the authorized A7.2 merge and checks its exact source and destinations; other member tests are unchanged. Exact implementation and verification evidence belongs in the PR handoff.'
assert s.count(a)==1;p.write_text(s.replace(a,b,1))
p=Path('delivery/teaching-revision.md');s=p.read_text()
s+='\n\nThe initial run correctly rejected the old 15-lesson inventory expectation after the approved merge removed A7.2. The updated inventory test expects 14, verifies 76 distinct components and 65 unique teaching entries, and checks the exact source commit, blob, absence of the duplicate, and retained destinations. Other member-document tests and the original historical-recovery inventory are unchanged. No test was skipped.\n'
p.write_text(s)
print('Updated only the authorized merged-lesson inventory contract; all other member tests preserved.')

#!/usr/bin/env python3
"""Apply the owner's reviewed voice-only patches; never edit generated copies first."""
from pathlib import Path
from collections import Counter
import importlib.util, hashlib, json, re, subprocess, sys
BASE='f9cf0c9fa48a29622708b18891edde99ead26db3'
root=Path.cwd()
spec=importlib.util.spec_from_file_location('course',root/'tools/guided_course.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
patch_file=Path(sys.argv[1])
patches=json.loads(patch_file.read_text())
# Clause-preserving contractions. Do not contract bare pronoun/copula endings.
contractions={
 'does not':"doesn't",'do not':"don't",'is not':"isn't",'are not':"aren't",
 'cannot':"can't",'will not':"won't",'would not':"wouldn't",'should not':"shouldn't",
 'we will':"we'll",'you will':"you'll",'they will':"they'll",'I would':"I'd",
 'we have':"we've",'you have':"you've",'they have':"they've",
}
# Have only contracts when it introduces a past participle, not possession.
participle=r'(?:already |also |just |still )?(?:been|done|made|taken|chosen|completed|checked|counted|changed|used|received|kept|given|compared|entered|worked|saved|recorded|tested|assigned|paid|included|discussed|found|covered|created|decided|borrowed|invested)\b'
rows=g.catalog(root);by={r['id']:r for r in rows}
assert len(g.CORE_IDS)==25 and len(g.ADV_IDS)==8 and len(g.PRACTICAL_IDS)==11
assert set(patches)==set(g.CORE_IDS+g.ADV_IDS)-{'2.3'}
# Protect explicit money/security warning phrasing and the illustrative family letter.
protected_starts=("This is financial education,", '“If I\'m unavailable,')
num=re.compile(r'\$?\d+(?:,\d{3})*(?:\.\d+)?(?:%|½)?')
allowed_removed={'1.2':Counter({'$155,000':1,'0.06':1}),'1.5':Counter({'790':1,'1,000':1,'100':1})}
updates={};report=[]
for r in rows:
 p=root/r['path'];base=subprocess.check_output(['git','show',BASE+':'+r['path']],cwd=root).decode()
 if p.read_text()!=base:raise ValueError('Unexpected preexisting source edit '+r['id'])
 if r['id'] not in patches:continue
 before=r['read'];after=before;count=0
 for old,new in patches[r['id']]:
  if after.count(old)!=1:raise ValueError(f"Patch not unique: {r['id']} {old[:100]!r}: {after.count(old)}")
  after=after.replace(old,new,1);count+=1
 paragraphs=after.split('\n\n')
 for i,paragraph in enumerate(paragraphs):
  if paragraph.startswith(protected_starts):continue
  for old,new in contractions.items():
   expr=r'\b'+re.escape(old)+r'\b'
   if old.endswith(' have'):expr+=r'(?=\s+'+participle+r')'
   def replace(m):return new[0].upper()+new[1:] if m[0][0].isupper() else new
   paragraph,n=re.subn(expr,replace,paragraph,flags=re.I);count+=n
  # Predicate follows, avoiding 'than you are', 'what it is', etc.
  for old,new in [('It is',"It's"),('That is',"That's"),('There is',"There's"),('They are',"They're"),('We are',"We're")]:
   paragraph,n=re.subn(r'(?<!\w)'+old+r'(?=\s+[A-Za-z0-9$])',new,paragraph);count+=n
  paragraph,n=re.subn(r'\bSuppose\b',"Let's say",paragraph);count+=n
  paragraph,n=re.subn(r'\bsuppose\b','say',paragraph);count+=n
  paragraph=paragraph.replace('Now say ',"Now let's say ")
  paragraph,n=re.subn(r'\bgenuinely available\b','actually available',paragraph);count+=n
  for old,new in [('if it is',"if it's"),('If it is',"If it's"),('whether it is',"whether it's"),('before it is',"before it's"),('but it is',"but it's"),('day it is',"day it's"),('while it is',"while it's"),('how it is',"how it's"),('that it is',"that it's"),('it is prepared',"it's prepared"),('they are',"they're"),('we are',"we're"),('you are',"you're")]:
   paragraph,n=re.subn(r'\b'+re.escape(old)+r'\b(?=\s+[A-Za-z0-9$])',new,paragraph);count+=n
  for old,new in [('rather than impersonate the owner or improvise','instead of impersonating the owner or improvising'),('rather than distributed outright','instead of being distributed outright'),('rather than automatically choose','instead of automatically choosing'),('rather than immediately refill','instead of immediately refilling'),('rather than assume','instead of assuming'),('rather than add','instead of adding'),('rather than pretend','instead of pretending'),('rather than borrow','instead of borrowing'),('rather than select','instead of selecting'),('rather than let','instead of letting'),('rather than make up','instead of making up'),('rather than discover','instead of discovering'),('rather than replace','instead of replacing'),('rather than copy','instead of copying'),('rather than repeat','instead of repeating'),('rather than infer','instead of inferring'),('rather than leave','instead of leaving'),('rather than stop','instead of stopping'),('rather than wait','instead of waiting')]:
   paragraph,n=re.subn(r'\b'+re.escape(old)+r'\b',new,paragraph);count+=n
  paragraph,n=re.subn(r'\brather than\b','instead of',paragraph);count+=n
  paragraphs[i]=paragraph
 after='\n\n'.join(paragraphs)
 for paragraph in before.split('\n\n'):
  if paragraph.startswith(protected_starts):assert paragraph in after,'Protected wording changed'
 # Verify numbers mechanically; two reviewed basic-arithmetic compressions omit repeated operands only.
 removed=Counter(num.findall(before))-Counter(num.findall(after));added=Counter(num.findall(after))-Counter(num.findall(before))
 assert not added,(r['id'],'added numbers',added)
 assert removed==allowed_removed.get(r['id'],Counter()),(r['id'],'unexpected removed numbers',removed)
 assert len(before.split('\n\n'))==len(after.split('\n\n')),(r['id'],'paragraph sequence changed')
 assert before in base
 updated=base.replace(before,after,1)
 # Metadata, sources, routes, checkpoints and all other sections remain byte-identical.
 assert base.replace(before,'<READ ALOUD>',1)==updated.replace(after,'<READ ALOUD>',1)
 updates[r['path']]=updated
 report.append({'id':r['id'],'edits':count,'before_words':len(before.split()),'after_words':len(after.split()),'before_sha256':hashlib.sha256(base.encode()).hexdigest(),'after_sha256':hashlib.sha256(updated.encode()).hexdigest()})
for path,text in updates.items():(root/path).write_text(text)
# One owner-direction note. Do not change the approved mapping or source authority.
authority=root/'AUSTIN-AUTHORITY.md'
base_authority=subprocess.check_output(['git','show',BASE+':AUSTIN-AUTHORITY.md'],cwd=root).decode()
assert authority.read_text()==base_authority
authority.write_text(base_authority.rstrip()+'''\n\n## Voice-only follow-up\n\nAustin accepted the consolidated content and structure and authorized voice edits only. Keep the 25 main and eight situation-specific recordings, their examples, financial assumptions, decision methods, and app handoffs. Apply natural spoken phrasing and rhythm without introducing new personal stories or preferences. Claude's substantive suggestions are not adopted by this authorization. The accepted Reserve remains unchanged; actual app and device capture remain separate.\n''')
g.build(root)
after_rows=g.catalog(root);after_by={r['id']:r for r in after_rows}
for lid in by:
 assert by[lid]['title']==after_by[lid]['title'] and by[lid]['path']==after_by[lid]['path']
 if lid in g.ADV_IDS:assert g.situation_route(by[lid])==g.situation_route(after_by[lid])
 if lid not in patches:assert by[lid]['text']==after_by[lid]['text']
assert g.member_order(rows)==g.member_order(after_rows)
assert (root/'DICTATION-ORDER.md').read_bytes()==subprocess.check_output(['git','show',BASE+':DICTATION-ORDER.md'],cwd=root)
assert (root/'FILM-ORDER.md').read_bytes()==subprocess.check_output(['git','show',BASE+':FILM-ORDER.md'],cwd=root)
print(json.dumps({'base':BASE,'changed_teaching_scripts':len(report),'editing_operations':sum(r['edits'] for r in report),'before_words':sum(r['words'] for r in rows if r['id'] in g.CORE_IDS+g.ADV_IDS),'after_words':sum(r['words'] for r in after_rows if r['id'] in g.CORE_IDS+g.ADV_IDS),'scripts':report},indent=2))

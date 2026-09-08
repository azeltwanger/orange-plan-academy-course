import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
p=root/'tools/_completion_edits_02_05.json'
rows=json.loads(p.read_text())
fixes={('2.1','In the working session'):'The working-session chapter takes',('2.4','In the working session'):'The working session will build',('2.5','In the working session'):'The app may model education events',('3.1','For the Reed'):'That ratio looks modest',('3.3','For the Reed'):'The Reed teaching plan directs'}
for row in rows:
    for change in row.get('changes',[]):
        key=(row['id'],change['starts'])
        if key in fixes:change['starts']=fixes.pop(key)
assert not fixes,'Unexpected already-changed patch data'
p.write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
Path(__file__).unlink()

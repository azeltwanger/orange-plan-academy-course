# These functions are integrated into the existing generator; this staging file is removed.
MERGED_LESSON = {
    'id':'A7.2',
    'path':'scripts/advanced/A7-2_decide-which-custody-responsibilities-the-household-can-maintain.md',
    'source_commit':'f6392a6341c23c557e605506dab3530b67efa146',
    'blob':'0443c4640a4f4b431429eab204f5fe9dc0b67413',
    'destinations':['7.1','7.4','W07'],
}

def situation_route(row: dict) -> dict:
    values={}
    for key,heading in [('after','After lesson'),('when','Use when'),('before','Complete before'),('return','Return to')]:
        found=re.findall(r'^'+re.escape(heading)+r': (.+)$',row['text'],re.M)
        if len(found)!=1 or not found[0].strip():
            raise ValueError('Missing or duplicate situation route '+row['id']+': '+heading)
        values[key]=found[0].strip()
    if values['after'] not in CORE_IDS or values['after'].split('.')[0]!=row['id'][1:].split('.')[0]:
        raise ValueError('Invalid parent lesson '+row['id'])
    if not re.search(r'^Kind: conditional$',row['text'],re.M):
        raise ValueError('Situational lesson is not marked conditional '+row['id'])
    return values

def member_order(rows: list[dict]) -> list[str]:
    by={r['id']:r for r in rows}; ordered=[]
    routes={lid:situation_route(by[lid]) for lid in ADV_IDS}
    for lid in CORE_IDS:
        ordered.append(lid)
        ordered.extend(x for x in ADV_IDS if routes[x]['after']==lid)
    if len(ordered)!=len(CORE_IDS)+len(ADV_IDS) or set(ordered)!=set(CORE_IDS+ADV_IDS):
        raise ValueError('Member sequence duplicates or omits a lesson')
    return ordered

def read_link(row: dict) -> str:
    group='advanced' if row['id'] in ADV_IDS else 'core'
    return f"teleprompter/{group}/{row['id'].replace('.','-')}.txt"

def situation_card(row: dict) -> str:
    r=situation_route(row)
    return (f"> **For your situation — [{row['title']}]({read_link(row)})**\n>\n"
            f"> {r['when']}\n>\n> {r['before']}\n>\n> **Return to:** {r['return']}.\n\n")

def review_state(row: dict) -> str:
    if row['id']=='2.3':return 'Accepted reference; unchanged'
    if 'Status: SPOKEN_EDIT_REVIEW' in row['text']:return 'Spoken-language edit; owner review pending'
    if 'Status: TEACHING_RETAINED_REVIEW' in row['text']:return 'Existing explanation retained; owner review pending'
    if 'Status: WALKTHROUGH_REWRITE_REVIEW' in row['text']:return 'Prepared narration; review and capture pending'
    if 'Status: TEACHING_REWRITE_REVIEW' in row['text']:return 'Written draft; owner review pending'
    return 'Review status requires attention'

def outputs(root: Path) -> dict[str,str]:
    rows=catalog(root);by={r['id']:r for r in rows};result={}
    routes={x:situation_route(by[x]) for x in ADV_IDS}
    order=member_order(rows)
    records=[]
    for r in rows:
        record={k:v for k,v in r.items() if k not in ('read','text','checkpoint')}
        if r['id'] in routes:record['member_route']=routes[r['id']]
        record['member_group']='For your situation' if r['id'] in ADV_IDS or r['id']=='2.5' else 'Main path' if r['id'] in CORE_IDS else 'Walkthrough'
        records.append(record)
    manifest={'canonical':'scripts/','source_commit':SOURCE_SHA,'app_contract_commit':APP_SHA,
              'counts':{'core':len(CORE_IDS),'advanced':len(ADV_IDS),'working_sessions':10,'device_demos':1},
              'member_labels':{'core':'Main path (includes the conditional college lesson)','advanced':'For your situation'},
              'member_order':order,'merged_lessons':[MERGED_LESSON],'lessons':records}
    result['COURSE-MANIFEST.json']=json.dumps(manifest,indent=2,ensure_ascii=False)
    editor_intro='Generated from `scripts/`. Spoken text is under Read aloud; production notes and checkpoints are not narration. Owner review and actual app/device recording remain separate.\n\n'
    result['MASTER-COURSE.md']='# Main course — teaching and production notes\n\n'+editor_intro+'The main path includes one conditional college lesson. Related situation-specific lessons are placed in the reading and playback orders where their decisions arise.\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in CORE_IDS)
    result['MASTER-ADVANCED.md']='# For your situation — collected teaching notes\n\n'+editor_intro+'This is a reference index, not a second course or a higher level. The A-prefixed IDs and filename are retained for existing links. Use a lesson when its stated situation applies, then return to the indicated walkthrough.\n\n'+'\n\n---\n\n'.join(by[x]['text'].strip() for x in ADV_IDS)
    spoken='# Course reading copy\n\nFollow the main path. For your situation lessons appear beside the decision they support. Read their condition: when your plan relies on that strategy, complete the extra lesson before relying on it; otherwise continue. Navigation notes are not spoken.\n\n'
    for x in order:
        r=by[x]
        spoken+='---\n\n'
        if x in routes:
            rr=routes[x]
            spoken+=f"*For your situation — {rr['when']} {rr['before']} Return to {rr['return']}.*\n\n"
        elif x=='2.5':
            spoken+='*For your situation — you intend to help fund education. Otherwise continue to Debt. Return to W02 chapter 7, then lesson 3.1.*\n\n'
        spoken+=f"## {x} — {r['title']}\n\n{r['read']}\n\n"
    result['ALL-SCRIPTS.md']=spoken
    for r in rows:
        result['lesson-text/'+r['path'].split('scripts/',1)[1]]=r['text']
        if r['read']:result[read_link(r)]=r['read']
    for m in range(11):
        module=f'# Session {m} — {NAMES[m]}\n\nMain lessons build the plan in order. Read an additional lesson only when its stated situation applies; then return to the indicated working chapter. These are draft teaching and production notes.\n\n'
        for x in CORE_IDS:
            if not x.startswith(str(m)+'.'):continue
            if x=='2.5':module+='> **For your situation:** You intend to help fund education. Otherwise continue to Debt.\n\n'
            module+=by[x]['text'].strip()+'\n\n'
            for a in ADV_IDS:
                if routes[a]['after']==x:
                    module+='---\n\n## For your situation\n\n'+routes[a]['when']+' '+routes[a]['before']+'\n\n'+by[a]['text'].strip()+'\n\n**Return to:** '+routes[a]['return']+'.\n\n'
            module+='---\n\n'
        result[f'modules/{m:02d}.md']=module
    reading='# Start here — course reading order\n\nWork through each main lesson and its matching walkthrough. **For your situation** identifies extra teaching for a decision you may or may not face. It is not a skill level. When you use that strategy, complete the lesson before relying on it; otherwise carry on. The Reserve remains the accepted reference; other wording is for owner review.\n\n'
    film='# Learning and filming order\n\nOne main path with situation-specific lessons beside the decisions they support. Read the main explanation, complete the relevant additional lesson when needed, then apply the decision in the matching working chapter. These written routes do not approve app/device capture or perform outside actions.\n\n'
    for m in range(11):
        reading+=f'## {m} — {NAMES[m]}\n\n';film+=f'## {m} — {NAMES[m]}\n\n'
        for x in CORE_IDS:
            if not x.startswith(str(m)+'.'):continue
            r=by[x];anchor='lesson-'+x.replace('.','-')
            optional=' — for households funding education' if x=='2.5' else ''
            reading+=f"### {x} — [{r['title']}]({read_link(r)}){optional}\n\n"
            film+=f'<a id="{anchor}"></a>\n\n'+f"### {x} — [{r['title']}]({r['path']}){optional}\n\n"
            if x=='2.5':
                note='No education commitment? Continue to lesson 3.1.\n\n';reading+=note;film+=note
            for a in ADV_IDS:
                if routes[a]['after']==x:
                    reading+=situation_card(by[a]);film+=situation_card(by[a])
            task=CHAPTERS.get(x,'W01 chapter 10 after the first plan is populated' if x=='0.2' else 'Orientation; no app entry')
            reading+='**Apply it:** '+task+'.\n\n'
            film+='**Working chapter:** '+task+'.\n\n'
    reading+='## Reference and recording notes\n\n[All situation-specific lessons](ADVANCED-DICTATION-ORDER.md) · [Paired working-session files](FILM-ORDER.md) · [Production checklist](PRODUCTION-CHECKLIST.md).\n\nThe internal paths retain `core` and `advanced` for link stability. Members follow the sequence above, not two separate courses. The former A7.2 responsibility lesson is included in 7.1, 7.4 and W07; it is not another required video.\n'
    result['DICTATION-ORDER.md']=reading
    reference='# For your situation — reference index\n\nThese lessons are placed beside the relevant main lesson in [the course reading order](DICTATION-ORDER.md). Use the situation, not your experience level, to choose. When a plan depends on the strategy, its extra analysis and safeguards are required for that choice. Otherwise skip it.\n\n'
    for x in order:
        if x not in routes:continue
        r=by[x];rr=routes[x]
        reference+=f"## [{r['title']}]({read_link(r)})\n\nAfter lesson {rr['after']}. {rr['when']}\n\n{rr['before']}\n\n**Return to:** {rr['return']}.\n\n[Teaching and demonstration notes]({r['path']}).\n\n"
    reference+='The college lesson is already beside Life Events in Session 2. Custody responsibilities formerly in A7.2 are now part of 7.1, 7.4 and W07, not a separate lesson. Legacy A IDs and this filename preserve existing references; they do not indicate a second program.\n'
    result['ADVANCED-DICTATION-ORDER.md']=reference
    film+='## Working-session files\n\n'+''.join(f"- [{x} — {by[x]['title']}]({by[x]['path']}) — recording evidence pending\n" for x in PRACTICAL_IDS)
    result['FILM-ORDER.md']=film
    result['CIRCLE-STRUCTURE.md']=film.replace('# Learning and filming order','# Member playback structure',1)
    result['SCREEN-SHOOT-LIST.md']='# Screen and device production list\n\nUse the route in FILM-ORDER.md. Applicable situation-specific instruction comes before relying on the strategy or executing its dependent action. All practical recordings still require actual evidence in CAPTURE-RECEIPTS.md.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n[Run sheet]({by[x]['path']})\n\n{by[x]['checkpoint']}\n\n" for x in PRACTICAL_IDS)
    result['MODULE-CHECKPOINTS.md']='# Member completion checks\n\nMain decisions and situation-specific applications are shown in learning order. A required professional answer or an unverified access route is not a completed action.\n\n'+''.join(f"## {x} — {by[x]['title']}\n\n"+(f"For your situation: {routes[x]['when']}\n\n" if x in routes else '')+by[x]['checkpoint']+'\n\n' for x in order+PRACTICAL_IDS)
    result['PRODUCTION-CHECKLIST.md']='# Production checklist\n\nOne main path, with applicable extra lessons routed at the relevant decision. The language pass does not establish Austin approval, instructional effectiveness or capture readiness. A7.2 is merged into 7.1/7.4/W07 and excluded from active recording counts.\n\n| ID | Script | Text review | Austin approval | Remaining publication gate |\n|---|---|---|---|---|\n'+''.join(f"| {r['id']} | [{r['title']}]({r['path']}) | {review_state(r)} | {'Reference accepted; filming separate' if r['id']=='2.3' else 'Pending'} | {r['gate']} |\n" for r in rows)
    main=sum(by[x]['words'] for x in CORE_IDS);extra=sum(by[x]['words'] for x in ADV_IDS)
    result['COURSE-METRICS.md']=f'# Current course inventory\n\n{len(CORE_IDS)} main-path teaching files include one conditional college lesson: 50 shared-path lessons plus college when relevant. There are {len(ADV_IDS)} additional For your situation lessons placed within their sections, ten app working sessions and one device demonstration. Total active teaching lessons: {len(order)}. A7.2 has been merged, not hidden in a second course.\n\nMain-path spoken text including college: {main:,} words. Situation-specific text: {extra:,} words. Approximate narration at 150 words/minute: {main/150:.0f} and {extra/150:.0f} minutes respectively. These are reading estimates, not promised runtimes or proof of value; walkthroughs and pauses are additional. Members do not need every situation-specific lesson.\n'
    return {p:t.rstrip()+'\n' for p,t in result.items()}


def merged_history(root: Path) -> None:
    item=MERGED_LESSON
    data=subprocess.check_output(['git','show',item['source_commit']+':'+item['path']],cwd=root)
    actual=hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
    if actual!=item['blob']:raise ValueError('Merged A7.2 source history differs')
    if (root/item['path']).exists():raise ValueError('Merged A7.2 restored as duplicate active lesson')
    print('PASS: merged A7.2 recovered byte-for-byte; active teaching is in 7.1, 7.4 and W07.')

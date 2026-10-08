# First Syllabus Test: ENTR 200

- PDF extraction preserved the schedule and project descriptions.
- The AI correctly flagged conflicting Project 1 deadlines:
  August 31 at 11:59 p.m. EDT on page 4 versus August 30 on page 14.
- The deadline should remain unresolved until the student confirms it.
- The presentation output needs improvement: it selected September 1
  even though its notes list both September 1 and September 3.

- Project 2: The AI correctly extracted September 28, 2026,
  at 11:59 p.m. EDT, but incorrectly described October 1 as
  a conflicting deadline. October 1 is a class meeting date.
- Improvement needed: distinguish class dates in the left column
  from assignment deadlines in the right column.


- After switching to text-block extraction, Project 2 returned
  September 28, 2026, at 11:59 p.m. EDT without a false conflict.
- Changing the prompt alone did not fix this example; improving
  the PDF reading order did. Other assignments still need checking.

- The latest output correctly flags Project 1's conflicting
  submission deadlines, but omits its presentation dates:
  September 1 and September 3.


- The latest output includes both Project 1 presentation dates,
  but creates separate items for September 1 and September 3.
- Expected: one presentation item with an unresolved date and
  both possible dates in notes, pending student confirmation.
- Output structure also varies between runs: type labels and
  source_page formats need a consistent schema.

- Schema validation passed for all 17 returned items.
- Project 1 presentation now correctly appears as one item with
  due_date null and candidate dates September 1 and September 3.
- Project 1 submission preserves both conflicting dates.
- Remaining issue: submission time is 23:59, but timezone is null
  despite EDT being stated for the August 31 deadline.
- Full accuracy and completeness have not yet been checked.

## First Ground-Truth Comparison

- All 17 labeled items matched exactly one AI entry.
- Due dates matched in 17/17 items, including unresolved dates.
- Due times matched in 16/17 items.
- Timezones matched in 9/17 items, but all nine matches were
  empty values. The AI missed all eight explicit EDT values.
- Project 1's submission time should remain unresolved at the
  item level; 23:59 belongs specifically to the August 31 option.
- Candidate dates, source pages, labels, and weights remain unscored.
- This syllabus was used to refine the prompt, so these results
  do not measure performance on unseen syllabi.

## Run After Timezone Prompt Update

- Schema validation passed for 16 items.
- Found 16 of 17 ground-truth items; omitted the questionnaire.
- Among matched items: dates 16/16, times 16/16,
  and timezones 15/16 matched.
- Incorrectly assigned EDT to Project 1's presentation.
- Quiz matching was updated to recognize the observed
  "Quiz 1–4" titles alongside "Module 1–4".
- Improved field accuracy came with reduced item coverage.
- Other fields remain unscored.

## TDM 101: First Test

- Schema validation passed, but the response contained only
  the Syllabus Quiz and Academic Integrity Quiz.
- It omitted the 14 weekly projects and 3 Outside Event reflections.
- The syllabus describes a usual project deadline of nine days
  after Monday release, at 11:55 p.m. Eastern, with exceptions.
- Missing exact dates should not cause assignments to be omitted.
- Recurring work must be represented without inventing deadlines.

## TDM 101: After Recurring-Work Prompt Update

- Schema passed with 19 items, matching the expected count.
- Inspected Weekly Project 1 and Outside Event Reflection 1;
  both correctly leave exact dates unresolved.
- Reflection 1 preserves the monthly requirement and the
  within-one-week-of-attendance rule.
- Project 1 preserves 23:55 but omits the structured timezone.
- Its notes should explicitly preserve the nine-day interval,
  deadline exceptions, and reference to the current schedule.
- The other 17 entries have not yet been reviewed.
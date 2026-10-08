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
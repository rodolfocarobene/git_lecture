## Batch 5 of exercises

1. Go back to your repository and in the settings section add a rule to protect
   the main branch! It must not be possible to push directly to main, a Pull
   Request (PR) must be required.

2. Add an issue to your repository, metioning some feature to add or some nice
   thing that you would add to the `README.md`.

3. Create a branch from main, adding the features mentioned in the issue. push
   the branch and create a PR fixing that issue. Open the PR in draft mode,
   assign yourself and then make it ready to be reviewed. Merge it. Remove the
   remote branch and remove it locally. Pull the changes in main.

4. Add the pre-commit action from _https://pre-commit.ci/_. Add a new custom
   action to launch `pytest tests/` on push. Test it in a new PR in your
   repository.

5. Fork this repository (you can remove the cloned one) and then clone it
   locally. Create a branch from the **test_it_yourself** branch and add a file
   in the students folders following the provided template. Push the new branch
   and open a PR in my repository, asking for review and merge (**CAREFUL: TO
   THE TEST_IT_YOURSELF branch, NOT MAIN**).

6. Review the PR of some other student and merge it, if it meets all the
   requirements. Otherwise, ask for changes.

## Batch 2 of exercises

1. Add a `.gitignore` file to your project, excluding `__pycache__` folders or
   whatever.

2. Create a new branch. Start modifying some file (README, pyrpoject.toml...).
   Before commiting, stash the changes and go back to main. Go back to your
   branch, unstash the changes and commit them. Try this with different
   strategies:

   - single stash and `stash pop`
   - multiple stashes with custom names
   - `stash apply` and `stash drop`

3. Try to change a file then, before commiting, restore the changes. Tr both
   with staged and not-staged changes.

4. Git blame some file and look at the output. Try isolating a single line.

5. Create a new branch from main and use `git cherrypick` to include some
   changes from the branch of exercise 1.

6. Add a new file, commit it and then use `git rm` or `git rm --cached` to
   remove it.

7. Add a bug to the TicTacToe game, commit it. Add a couple of commit more and
   try to identify the problematic commit with `git bisect`. Note that you can
   run tests using `pytest tests` to see if a bug is present or not. Use both
   the manual way and the `git bisect run <cmd>` way.

8. Add a tag to the project. Version `v0.0.1` or what you prefer.

9. Find your `.gitconfig` file and have a look!

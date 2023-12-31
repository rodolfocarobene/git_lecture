## Batch 3 of exercises

1. Add a `post-commit` hook to print something like "New Commit added!" whenever
   you do a commit. Tip: in bash, to print a string you use
   `echo "<my_string>"`. To make a script executable, you need to use
   `chmod +x <nome_script>`.

2. Install pre-commit and setup a `.pre-commit-config.yaml` file including
   useful hooks. Try them out writing some badly formatted code and trying to
   commit it. It should automatically fix it, does it?

3. Setup some git aliases that you find useful. Look in the `.gitconfig` file
   where they should be stored.

4. Do a commit, remove it with `git reset`, re-do it with a different commit
   message.

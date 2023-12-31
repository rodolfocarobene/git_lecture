## Batch 1 of exercises

1. Check Git is installed, otherwise install it!

2. Configure Git with basic settings:

   ```bash
   git config --global user.name "Bugs Bunny"
   git config --global user.email bugs@gmail.com
   git config --global core.editor notepad
   git config --global init.defaultbranch main
   git config --global credential.helper store
   ```

3. Create a new empty repository for a project of TicTacToe with a README.md
   file. Commit it in a branch called `main`!

4. Create a new branch called `structure` and in that branch add the following
   structure of files:

   - `pyproject.toml`
   - `src/tictactoe/__init__.py`
   - `src/tictactoe/game.py`
   - `tests/test_game.py`

   If you want it, you can try to code them yourself, otherwise all the files
   are already present in the [batch1](batch1) subfolder!.

   Remember to check `git status` every now and then, in order to have full
   control of the commit workflow.

   Commit all the changes you have made.

   Check the code runs properly by installig it with `pip install -e .` and then
   by running the tests `pytest tests`.

5. Merge the `structure` branch into `main` and then delete it.

6. Create a basic conflict (modifying the same line of a file in two branches)
   and solve it.

7. See the log history with `git log`, use `git checkout` to jump to an older
   commit and check the diff (`git diff`) between that commit and the last one.

   You can use, for example, the empty README.md!

8. Look at the command you just learnt and run `git <command> --help`. Do you
   find interesting information? Look into `git log --help` and try to use some
   option to beautify the output of the command.

9. Look into `git commit --help` and try to use some option to change the
   message of the last commit.

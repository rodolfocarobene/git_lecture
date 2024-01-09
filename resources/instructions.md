# Preliminary instructions

During the git-GitHub seminar, I will show you various examples of git commands
and operative workflows. Moreover, we will have various sessions of "exercises"
where you will try the newly learnt commands/features.

For these reason, it is important to arrive prepared: you will need to:

- install git
- create an account on GitHub

## Git installation

You can find complete instructions on
[the official webiste](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

First open a terminal (on Windows both commandprompt and powershell should work)
and check if `git` is installed by running:

```bash
git --version
```

If the package is missing, it will throw an error.

### Windows

You can download `git` from the official
[website](https://git-scm.com/download/win). You should see a "Click here to
download the latest..." clickable link, if your computer is not x64, use the
"standalone installer" below.

You will then have to go through a fast configuration phase, leave everything as
default except to:

- "Choosing the default editor used by Git": select your editor of preference
  (notepad or notepad++ for example)
- "Adjusting the name of the initial branch in new repositories": select the
  custom option and write "main"

### macOS

On Mavericks (10.9) or above, running the `git --version` command from a
terminal should already have installed the package if it was missing

If that didn't work, try to install
[xcodes](https://developer.apple.com/xcode/), this package should ship with git
and makes a pretty nice IDE.

### Linux

On Debian-based distribution (such as Ubuntu) you just need to run, from a
terminal:

```bash
sudo apt-get install git
```

## Create GitHub profile

If you still don't have it, create a GitHub profile from the
[Signup page](https://github.com/signup).

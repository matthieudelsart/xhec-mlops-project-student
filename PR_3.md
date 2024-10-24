Before working on this branch, include your previous work from steps 1 and 2 (which have been merged to the main branch) in your branch:

```bash
git checkout 3/use_prefect
git pull origin master
git push
```

> Note: you can also use a `rebase` if you are familiar with this command.

The goal of this PR is to:

- [x] Use the prefect library to adapt the code developed in the PR2 to use `flow` and `task` objects
- [x] Create a deployment to retrain the model regularly

Files to be modified: the `src/modelling` folder

- [x] Don't forget to update the `requirements.in` and `requirements-dev.in` files with the new dependencies (and compile them)
- [x] Don't forget to update the `README.md` file with the new steps to reproduce to run the code
- [x] You should among other add instructions to run the prefect UI and visualize the flow runs

___
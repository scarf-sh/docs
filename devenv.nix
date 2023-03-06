{ pkgs, ... }:

{
  # https://devenv.sh/basics/
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = [
    pkgs.git
  ];

  enterShell = ''
    pip install -r requirements.txt
  '';

  # https://devenv.sh/languages/
  languages.python.enable = true;
  languages.python.venv.enable = true;

  # https://devenv.sh/pre-commit-hooks/
  pre-commit.hooks.markdownlint.enable = true;

  # https://devenv.sh/processes/
  # processes.ping.exec = "ping example.com";
  processes.serve.exec = "mkdocs serve";
}
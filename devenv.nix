{ pkgs, ... }:

{
  env.GREET = "devenv";

  packages = [
    pkgs.git
  ];

  enterShell = ''
    pip install -r requirements.txt
  '';

  languages.python.enable = true;
  languages.python.venv.enable = true;

  processes.serve.exec = "mkdocs serve";
}

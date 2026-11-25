{
  pkgs,
  config,
  inputs,
  ...
}: let
  pkgs-convco = import inputs.nixpkgs-convco {system = pkgs.stdenv.system;};
in {
  name = config.env.SERVICE_NAME;
  env.GREET = "devenv";

  # https://devenv.sh/packages/
  packages = with pkgs; [
    git
  ];

  cachix.pull = ["rbabaev"];

  difftastic.enable = true;

  git-hooks.hooks = {
    alejandra.enable = true;
    check-toml.enable = true;
    convco = {
      enable = true;
      package = pkgs-convco.convco;
    };
    deadnix.enable = true;
    shellcheck.enable = true;
    shfmt.enable = true;
  };
}

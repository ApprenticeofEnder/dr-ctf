{
  pkgs,
  config,
  ...
}: {
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
    convco.enable = true;
    deadnix.enable = true;
    shellcheck.enable = true;
    shfmt.enable = true;
  };
}

{...}: {
  env = {
    API_PORT = 8000;
    SERVICE_NAME = "dr-ctf-api";
  };

  languages = {
    python = {
      enable = true;
      uv = {
        enable = true;
      };
    };
  };

  git-hooks.hooks = {
    pyright.enable = true;
    ruff.enable = true;
    ruff-format.enable = true;
    uv-check.enable = true;
    uv-export = {
      enable = true;
      settings = {
        format = "requirements.txt";
      };
    };
    uv-lock.enable = true;
  };
}

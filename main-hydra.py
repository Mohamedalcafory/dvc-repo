import hydra
from omegaconf import DictConfig, OmegaConf as omc

@hydra.main(config_path="configs", config_name="config", version_base='1.3')
def main(cfg: DictConfig) -> None:
    print(omc.to_yaml(cfg))

if __name__ == "__main__":
    main()
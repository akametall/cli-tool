import ruamel.yaml as yaml
import sys
import click


@click.command()
@click.option(
    "--input_file",
    "--i",
    "--in",
    required=True,
    type=click.File("r"),
    help="Path to yaml file to be processed.",
)
@click.option(
    "--output_file",
    "--o",
    "--out",
    default="./new_SOL.yaml",
    show_default=True,
    type=click.File("w"),
    help="Path to yaml file to store the result.",
)
def main(input_file, output_file):
    origin = input_file.read()
    docs = yaml.safe_load_all(origin)
    docs_prepared = []
    for smth in docs:
        name = smth["metadata"]["name"]
        desc = smth["metadata"]["description"]
        config_in = {
            "apiVersion": "backstage.io/v1alpha1",
            "kind": "Component",
            "metadata": {"name": (name), "description": (desc)},
            "spec": {"type": "", "lifecycle": "", "owner": "", "system": ""},
        }
        docs_prepared.append(config_in)
    populate_config = yaml.dump_all(
        docs_prepared, default_flow_style=False, allow_unicode=True
    )
    config = validate_yaml(populate_config)

    encryption_config = output_file.open()
    encryption_config.write(config)
    encryption_config.close()
    print("OK")


def validate_yaml(config):
    try:
        yaml.safe_load_all(config)
        return config
    except:
        sys.exit("Failed to validate Yaml.")


if __name__ == "__main__":
    main()

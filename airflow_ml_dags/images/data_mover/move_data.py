import os
import click
import shutil

DATA_NAME = "data.csv"
TARGET_NAME = "target.csv"

@click.command()
@click.option("--input-dir")
@click.option("--output-dir")
def move_data(input_dir: str, output_dir: str):    
    os.makedirs(output_dir, exist_ok=True)
    shutil.move(os.path.join(input_dir, DATA_NAME), os.path.join(output_dir, DATA_NAME))
    shutil.move(os.path.join(input_dir, TARGET_NAME), os.path.join(output_dir, TARGET_NAME))

if __name__ == '__main__':
    move_data()
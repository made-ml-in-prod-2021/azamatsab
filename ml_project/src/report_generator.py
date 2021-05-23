import os
import sys
import logging

from pandas_profiling import ProfileReport
import pandas as pd
import hydra
from hydra.utils import to_absolute_path

from entities.config import ReportConfig
from utils import check_dir

logger = logging.getLogger("classifier.report_generator")


def generate_report(config: ReportConfig):
    out_path = to_absolute_path(config.output_path)
    in_path = to_absolute_path(config.input_path)
    data = pd.read_csv(in_path)
    profile = ProfileReport(data, title="Profiling Report", explorative=True)

    logger.info("Save report to %s", out_path)
    check_dir(os.path.split(out_path)[0])
    profile.to_file(str(out_path))


@hydra.main("conf", config_name="report_config")
def main(config: ReportConfig):
    generate_report(config)


if __name__ == "__main__":
    main()

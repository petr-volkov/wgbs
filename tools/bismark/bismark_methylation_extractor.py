__author__ = 'med-pvo'
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
import config.global_configs as global_configs


class BismarkMethylationExtractor():
    def __init__(self, input_file_path, output_dir=None, ncores=None):
        self.__input_file_path = input_file_path
        self.__output_dir = output_dir if output_dir else os.path.dirname(self.input_file_path)
        self.ncores = ncores

    @property
    def input_file_path(self):
        return self.__input_file_path

    @property
    def output_dir(self):
        return self.__output_dir

    def bismark_met_extractor_command(self):
        config = global_configs.project_config
        command = config.bismark_methylation_extractor_path
        command += " -p "
        command += " -o " + self.output_dir + " "
        command += self.input_file_path + " "
        command += "--samtools_path " + config.samtools_dir
        command += " --bedGraph "
        command += " --ample_memory "
        command += " --multicore " + str(int(self.ncores / 3)) if self.ncores else ""
        command += " > " + self.log_file_path()
        command += " 2>" + self.log_file_path()
        #command += " 2>/dev/null"
        return command

    def log_file_path(self):
        return os.path.join(self.output_dir, "methylation_extractor.log")


if __name__ == "__main__":
    bme = BismarkMethylationExtractor("/mnt/lustre/Home/petr_v/Projects/IsletsWGBS/Private/IsletsWGBS/AlignedResults/33_EpiGnome_1_ATCACG_L001_140513/33_EpiGnome_1_ATCACG_L001_140513.deduplicated.bam")
    print(bme.bismark_met_extractor_command())

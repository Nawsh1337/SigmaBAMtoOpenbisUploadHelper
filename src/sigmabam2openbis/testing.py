import os
import time
import pandas as pd
from bam_masterdata.datamodel.object_types import ExperimentalStep
from bam_masterdata.parsing import AbstractParser

class person():
    Age = None
    Sport = None
    Full_Name = None
    BMI = None

    def __repr__(self):
        return (
            f"person(Age={self.Age!r}, Sport={self.Sport!r}, "
            f"Full_Name={self.Full_Name!r}, BMI={self.BMI!r})"
        )

# class sigmabam2openbis(AbstractParser):
    # def parse(self, files, collection, logger):
    #     delay_seconds = float(os.getenv("OPENBIS_PARSER_EXAMPLE_DELAY_SECONDS", "0"))
    #     if delay_seconds > 0:
    #         logger.info("Artificial parser delay enabled.", delay_seconds=delay_seconds)
    #         time.sleep(delay_seconds)

    #     synthesis = ExperimentalStep(name="Synthesis")
    #     synthesis_id = collection.add(synthesis)
    #     measurement = ExperimentalStep(name="Measurement")
    #     measurement_id = collection.add(measurement)
    #     _ = collection.add_relationship(synthesis_id, measurement_id)
    #     logger.info(
    #         " USING THIS REPO, PARSER LUCAS Parsing finished: Added examples synthesis and measurement experimental steps."
    #     )






# class sigmabam2openbis(AbstractParser):
    # def parse(self, file, collection = None, logger = None):

        # df = pd.read_excel(file)
        # # print(df)

        # # print(df['First Name'])
        # # print(df['Last Name'])

        # df['Full Name'] = df['First Name'] + " " +  df["Last Name"]

        # # print(df)

        # df['BMI'] = df['Weight'].astype(float) / df["Height"].astype(float)

        # print(df)

        # df = df.drop(columns=["First Name", "Last Name", "Weight", "Height"])

        # print(df)

        # df.to_excel('output_testing.xlsx',index = False)








        # def parse(self, file, collection = None, logger = None):
        #     p1 = person()
        #     # print(p1)

        #     df = pd.read_excel(file,index_col=None)

        #     p1.Full_Name = df['First Name'] + " " +  df["Last Name"]


        #     p1.BMI = float()

        #     p1.Age = df['Age']
        #     p1.Sport = df['Sport']

        #     print(p1)

        #     collection.add(p1)




if __name__ == "__main__":
    print("Running OpenbisParserExample as a standalone script.")
    parser = sigmabam2openbis()
    input_file = "Sample_Input_For_Parser_tutorial.xlsx"#path
    collection = []  # Replace with an actual collection object if needed
    parser.parse(input_file)
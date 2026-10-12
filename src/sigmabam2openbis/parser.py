import re

import pandas as pd
from bam_masterdata.datamodel.object_types import Chemical
from bam_masterdata.parsing import AbstractParser


class OpenbisParserExample(AbstractParser):
    MAPPING_COLUMNS = {
        "Handelsname": "Name",
        "Synonyme": "Alternative Name",
        "CAS-Nr": "CAS Registry Number",
        "Hersteller": "Manufacturer",
        "Konzentration [%]": "Concentration",
        "Dichte [g/cm³]": "Density",
    }
    REQUIRED_COLUMNS = (*MAPPING_COLUMNS, "Umgang-Id", "Organisationseinheit")
    FINAL_COLUMNS = (
        "$",
        "Name",
        "Alternative Name",
        "CAS Registry Number",
        "Manufacturer",
        "Concentration",
        "Density",
        "IUPAC Name",
        "Supplier",
        "Lot/Batch Number",
        "External Barcode",
        "Description",
        "Product Category",
        "Hazardous Substance",
        "BAM Organizational Entity",
        "Complete BAM Location",
        "Responsible person",
        "Molar Mass",
        "Bottling Date",
        "Opening Date",
        "Expiration Date",
        "Empty",
        "Notes",
        "Comments",
        "Code",
        "Identifier",
    )
    DEFAULT_IDENTIFIER_PREFIX = "/VP.1_NARSHAD/PARSER_TEST"
    ALLOWED_PRODUCT_CATEGORIES = {
        "PC0", "PC1", "PC2", "PC3", "PC4", "PC7", "PC8", "PC9A", "PC9B",
        "PC9C", "PC11", "PC12", "PC13", "PC14", "PC15", "PC16", "PC17",
        "PC18", "PC20", "PC21", "PC23", "PC24", "PC25", "PC26", "PC27",
        "PC28", "PC29", "PC30", "PC31", "PC32", "PC33", "PC34", "PC35",
        "PC36", "PC37", "PC38", "PC39", "PC40", "PC41", "PC42",
    }
    HAZARD_COLUMNS = ("H-Sätze", "EUH-Sätze", "P-Sätze", "CMR")
    LOCATION_COLUMNS = ("Liegenschaft", "Haus", "Etage", "Raum-Nr")
    NOTE_COLUMNS = (
        "Piktogramme",
        "Reinheit",
        "Druck [Bar]",
        "max. Menge",
        "Konzentration [%]",
        "CMR",
        "H-Sätze",
        "EUH-Sätze",
        "P-Sätze",
    )
    DIVISIONS = (
        "1.1 Inorganic Trace Analysis",
        "1.2 Biophotonics",
        "1.3 Instrumental Analytics",
        "1.4 Process Analytical Technology",
        "1.5 Protein Analysis",
        "1.6 Inorganic Reference Materials",
        "1.7 Organic Trace and Food Analysis",
        "1.8 Environmental Analysis",
        "1.9 Chemical and Optical Sensing",
        "2.1 Safety of Energy Carriers",
        "2.2 Process Simulation",
        "2.3 Classification of Hazardous Substances and Dangerous Goods",
        "2.4 Testing and Evaluation of Explosives and Pyrotechnics",
        "2.5 Conformity Assessment Explosives and Pyrotechnics",
        "3.1 Safety of Dangerous Goods Packagings and Batteries",
        "3.2 Safety of Energy Storage Systems",
        "3.3 Safety of Transport Containers",
        "3.4 Safety of Storage Containers",
        "3.5 Safety of Gas Storage Systems and Tanks For Dangerous Goods",
        "3.6 Electrochemical Energy Materials",
        "4.1 Biodeterioration and Reference Organisms",
        "4.2 Material-Microbiome Interactions",
        "4.3 Molecular and Applied Entomology",
        "4.4 Thermochemical Residues Treatment and Resource Recovery",
        "4.5 Analysis of Artefacts and Cultural Assets",
        "5.1 Microstructural Design and Degradation",
        "5.2 Metallic High-Temperature Materials",
        "5.3 Polymer Matrix Composites",
        "5.4 Advanced Multi-materials Processing",
        "5.5 Materials Modelling",
        "5.6 Glasses",
        "6.1 Surface and Thin Film Analysis",
        "6.2 Material and Surface Technologies",
        "6.3 Structure Analysis",
        "6.4 Materials Informatics",
        "6.5 Synthesis and Scattering of Nanostructured Materials",
        "6.6 Digital Materials Chemistry",
        "6.7 Materials Synthesis and Design",
        "7.1 Building Materials",
        "7.2 Buildings and Structures",
        "7.3 Fire Engineering",
        "7.4 Technology of Construction Materials",
        "7.5 Technical Properties of Polymeric Materials",
        "7.6 Corrosion and Corrosion Protection",
        "7.7 Modelling and Simulation",
        "8.1 Sensors, Measurement and Testing Methods",
        "8.2 Non-Destructive Testing Methods For Civil Engineering",
        "8.3 Thermographic Methods",
        "8.4 Acoustic and Electromagnetic Methods",
        "8.5 X-Ray Imaging",
        "8.6 Fibre Optic Sensors",
        "9.1 Components For Energy Carriers",
        "9.2 Testing Devices and Equipment",
        "9.3 Welding Technology",
        "9.4 Weld Mechanics",
        "9.5 Tribology and Wear Protection",
        "9.6 Additive Manufacturing of Metallic Components",
        "S.1 Quality In Testing",
        "S.2 Digitalization of Quality Infrastructure",
        "S.3 Ecodesign and Energy Labelling",
        "Z.1 Organisation, Controlling",
        "Z.2 Budget",
        "Z.3 Human Resources",
        "Z.4 Education and Training, Health Management",
        "Z.5 Procurement",
        "Z.6 Internal Services",
        "Z.7 Buildings",
        "Z.8 Legal Services office, Library",
        "Z.9 Research Services",
    )
    CHEMICAL_PROPERTIES = {
        "Name": "name",
        "Alternative Name": "alias",
        "IUPAC Name": "iupac_name",
        "CAS Registry Number": "cas_number",
        "Manufacturer": "manufacturer",
        "Supplier": "supplier",
        "Lot/Batch Number": "lot_number",
        "External Barcode": "barcode_external",
        "Description": "description",
        "Product Category": "product_category",
        "Hazardous Substance": "hazardous_substance",
        "BAM Organizational Entity": "bam_oe",
        "Complete BAM Location": "bam_location_complete",
        "Responsible person": "responsible_person",
        "Molar Mass": "mass_molar",
        "Density": "density_gram_per_cubic_cm",
        "Concentration": "concentration",
        "Bottling Date": "date_bottling",
        "Opening Date": "date_opening",
        "Expiration Date": "date_expiration",
        "Empty": "substance_empty",
        "Notes": "notes",
        "Comments": "xmlcomments",
    }

    def parse(self, files, collection = None, logger = None):
        parsed_df = self.transform_files(files)
        print(parsed_df)

        for record in parsed_df.to_dict(orient="records"):
            chemical = Chemical(code=self._clean_text(record["Code"]))
            # print("code = ",self._clean_text(record["Code"]))

            print(f"Object type: {chemical.defs.code}")
            print(f"Object code: {chemical.code}")
            print(f"Object properties: {chemical.properties}")


            for column, property_name in self.CHEMICAL_PROPERTIES.items():
                value = record[column]
                if column == "Hazardous Substance" and value is not None:
                    value = value == "true"
                elif column == "Density":
                    value = self._parse_number(value)
                if not self._is_missing(value):
                    setattr(chemical, property_name, value)
            print()
            print()
            print(chemical)
            collection.add(chemical)

        # logger.info(
        #     "Local chemical parsing finished.",
        #     files=len(files),
        #     chemicals=len(parsed_df),
        # )

    def transform_files(self, files):
        if not files:
            raise ValueError("At least one Excel input file is required.")

        dataframes = []
        for file_path in files:
            source_df = pd.read_excel(file_path, header=0, engine="openpyxl", dtype=str)
            dataframes.append(self._transform_dataframe(source_df))
        return pd.concat(dataframes, ignore_index=True)

    def _transform_dataframe(self, source_df):
        missing_columns = [
            column for column in self.REQUIRED_COLUMNS if column not in source_df.columns
        ]
        if missing_columns:
            missing = ", ".join(missing_columns)
            raise ValueError(f"Required source column(s) missing: {missing}")
        if source_df.empty:
            raise ValueError("The Excel input contains no chemical rows.")

        output_df = pd.DataFrame(index=source_df.index)
        output_df["$"] = source_df["Umgang-Id"].map(
            lambda value: (
                f"${self._clean_text(value)}"
                if self._clean_text(value) is not None
                else None
            )
        )
        for source_column, output_column in self.MAPPING_COLUMNS.items():
            output_df[output_column] = source_df[source_column].map(self._clean_text)
        for column in self.FINAL_COLUMNS:
            if column not in output_df:
                output_df[column] = None
            else:
                output_df[column] = output_df[column].astype(object)

        for index, row in source_df.iterrows():
            hazard_values = (
                self._clean_text(row[column])
                for column in self.HAZARD_COLUMNS
                if column in source_df.columns
            )
            output_df.at[index, "Hazardous Substance"] = (
                "true" if any(hazard_values) else "false"
            )

            category = self._clean_text(row.get("Produktkategorie"))
            if category:
                category_code = category.split()[0]
                if category_code in self.ALLOWED_PRODUCT_CATEGORIES:
                    output_df.at[index, "Product Category"] = category_code

            location_parts = [
                self._clean_text(row[column])
                for column in self.LOCATION_COLUMNS
                if column in source_df.columns
            ]
            location = "/".join(part for part in location_parts if part)
            output_df.at[index, "Complete BAM Location"] = location or None

            handling_id = self._clean_text(row["Umgang-Id"])
            entity_code = self._clean_text(row["Organisationseinheit"])
            if handling_id and entity_code:
                output_df.at[index, "Code"] = (
                    f"CHEM-{entity_code}-{handling_id.zfill(4)}"
                )
            if entity_code:
                output_df.at[index, "BAM Organizational Entity"] = next(
                    (
                        division
                        for division in self.DIVISIONS
                        if division.startswith(f"{entity_code} ")
                    ),
                    None,
                )

            output_df.at[index, "Responsible person"] = self._responsible_person(
                row.get("AntragstellerIn")
            )
            output_df.at[index, "Concentration"] = self._parse_concentration(
                row["Konzentration [%]"]
            )
            output_df.at[index, "Identifier"] = (
                f"{self.DEFAULT_IDENTIFIER_PREFIX}/{output_df.at[index, 'Code']}"
                if output_df.at[index, "Code"]
                else None
            )

            notes = [
                f"{column}: {self._clean_text(row[column]) or 'None'}"
                for column in self.NOTE_COLUMNS
                if column in source_df.columns
            ]
            output_df.at[index, "Notes"] = " | ".join(notes) or None

        return output_df.loc[:, self.FINAL_COLUMNS]

    @staticmethod
    def _is_missing(value):
        return value is None or bool(pd.isna(value))

    @classmethod
    def _clean_text(cls, value):
        if cls._is_missing(value):
            return None
        text = str(value).strip()
        return text or None

    @classmethod
    def _parse_number(cls, value):
        text = cls._clean_text(value)
        if text is None:
            return None
        match = re.search(r"[-+]?[\d.,]+", text)
        if match is None:
            return None
        try:
            return float(match.group().replace(",", "."))
        except ValueError:
            return None

    @classmethod
    def _parse_concentration(cls, value):
        text = cls._clean_text(value)
        if text is None:
            return None
        text = text.replace("%", "").replace("<", "").replace(">", "")
        if "-" in text:
            return 0.0
        return cls._parse_number(text)

    @classmethod
    def _responsible_person(cls, value):
        name = cls._clean_text(value)
        if name is None:
            return None
        for original, replacement in {
            "ä": "ae",
            "ö": "oe",
            "ü": "ue",
            "Ä": "Ae",
            "Ö": "Oe",
            "Ü": "Ue",
        }.items():
            name = name.replace(original, replacement)
        parts = name.split()
        if len(parts) < 2:
            return None
        return f"/BAM_GLOBAL/BAM_DATA/{parts[-1][0].upper()}{parts[0][:7].upper()}"



if __name__ == "__main__":
    print("Running OpenbisParserExample as a standalone script.")
    parser = OpenbisParserExample()
    input_files = ["input.xlsx"]
    collection = []
    parser.parse(input_files, collection)
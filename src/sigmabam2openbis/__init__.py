from .parser import sigmabam2openbis

# Add more metadata if needed
sigmabam2openbis_entry_point = {
    "name": "sigmabam2openbis",
    "description": "An example parser for openBIS using the bam-masterdata infrastructure.",
    "parser_class": sigmabam2openbis,
}

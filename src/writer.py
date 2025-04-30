import os
import logging

logger = logging.getLogger(__name__)

class FileWriter:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def write(self, markdown, metadata):
        filename = metadata.get("title", "index") + ".md"
        path = os.path.join(self.output_dir, filename)
        with open(path, "w", encoding="utf-8") as f:
            f.write(markdown)
        logger.info(f"Written {path}")

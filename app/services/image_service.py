from pathlib import Path
import os

from fastapi import UploadFile

UPLOAD_DIR = Path("uploads/profile_images")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


class ProfileImageService:

    @staticmethod
    async def upload_or_update_image(
        email: str,
        file: UploadFile,
    ) -> str:
        """
        Uploads or replaces a profile image.
        Returns image url.
        """

        email_name = (
            email.lower()
            .replace("@", "_")
            .replace(".", "_")
        )

        extension = os.path.splitext(file.filename)[1]

        new_filename = f"{email_name}{extension}"

        # remove old image if exists
        for existing_file in UPLOAD_DIR.glob(f"{email_name}.*"):
            existing_file.unlink()

        file_path = UPLOAD_DIR / new_filename

        content = await file.read()

        with open(file_path, "wb") as image:
            image.write(content)

        return f"/uploads/profile_images/{new_filename}"
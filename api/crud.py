from scanner import Scanner


async def post(image):
    scanned_image = Scanner.scan(image)
    return scanned_image

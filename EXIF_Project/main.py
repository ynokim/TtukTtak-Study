from exif import Image
import webbrowser

# Open File
with open("20211221_125748.jpg", "rb") as file_read:
    image = Image(file_read)

# 위도와 경도
def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + coordinates[1] / 60 + coordinates[2] / 3600
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees

if image.has_exif:
    status = f"contains EXIF (version {image.exif_version}) information."
    maker = f"Camera manufacturer: {image.make}"
    model = f"Camera model: {image.model}"
    latitude = dms_coordinates_to_dd_coordinates(image.gps_latitude, image.gps_latitude_ref)
    longitude = dms_coordinates_to_dd_coordinates(image.gps_longitude, image.gps_longitude_ref)
    google_map = f"https://www.google.com/maps?q={latitude},{longitude}"
    kakao_map = f"https://map.kakao.com/?q={latitude},{longitude}"

print(f"image {status}")
print("=============================")
print(f"{maker}")
print(f"{model}")
print(f"위도(Decimal_degrees): {latitude}")
print(f"경도(Decimal_degrees): {longitude}")
print(f"Google Maps URL Link: {google_map}")
print(f"Kakao Map URL Link: {kakao_map}")
webbrowser.open_new_tab(kakao_map)

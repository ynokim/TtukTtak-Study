from exif import Image
import webbrowser

# Open File
with open("20211221_125748.jpg", "rb") as file_read:
    image = Image(file_read)

# 위도와 경도값을 도, 분, 초 값에서 decimal 값으로 계산
def dms_coordinates_to_dd_coordinates(coordinates, coordinates_ref):
    decimal_degrees = coordinates[0] + coordinates[1] / 60 + coordinates[2] / 3600
    if coordinates_ref == "S" or coordinates_ref == "W":
        decimal_degrees = -decimal_degrees

    return decimal_degrees

# 이미지에 exif가 있을 경우 정보 등록
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

# 이미지에 exif가 없을 경우 출력
else:
    status = f"not contains EXIF. "
    print(f"image {status}")

# 특정한 주소를 웹 브라우저에서 새 창으로 실행
webbrowser.open_new_tab(kakao_map)
webbrowser.open_new_tab(google_map)

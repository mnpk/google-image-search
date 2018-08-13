from google_image_search import GoogleAPI


def main():
    img_url = GoogleAPI.search_img("python")
    print(img_url)

    gif_url = GoogleAPI.search_gif("python")
    print(gif_url)


if __name__ == '__main__':
    main()

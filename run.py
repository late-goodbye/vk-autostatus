from generator import Generator
import vk_api
import time


if __name__ == '__main__':
    generator = Generator()

    while True:
        vk = vk_api.VkApi(token=generator.token)
        status = generator.generate_status()
        vk.method("status.set", {"text": status})
        print("Set status")
        time.sleep(60)

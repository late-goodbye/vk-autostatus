from generator import Generator
import vk_api
import time


generator = Generator()

while True:
    vk = vk_api.VkApi(token=generator.token)
    status = generator.generate_status()
    vk.method("status.set", {"text": status})
    print("Set status: {status}".format(status=status))
    time.sleep(30)

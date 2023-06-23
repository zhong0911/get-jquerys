import os
import get
import jquery


def main():
    num = 0
    for i in range(1, 4):
        for j in range(20):
            for k in range(20):
                try:
                    version = str(i) + "." + str(j) + "." + str(k)
                    print(version)
                    max_js = get.get_text(jquery.jquery + version + "/jquery.js")
                    min_js = get.get_text(jquery.jquery + version + "/jquery.min.js")
                    min_map = get.get_text(jquery.jquery + version + "/jquery.min.map")
                    slim = get.get_text(jquery.jquery + version + "/jquery.slim.js")
                    slim_map = get.get_text(jquery.jquery + version + "/jquery.slim.map")
                    list = [max_js, min_js, slim, min_map, slim_map]
                    for item in list:
                        os.mkdir(f"./jquery/{version}")
                        if item == '{"error":"Document not found"}':
                            print('')
                except Exception as e:
                    print(e)


if __name__ == '__main__':
    main()

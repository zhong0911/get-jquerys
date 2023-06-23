import os
import get
import jquery


def main():
    num = 0
    for i in range(1, 5):
        for j in range(3, 10):
            for k in range(10):
                try:
                    version = str(i) + "." + str(j) + "." + str(k)
                    url = jquery.cookie + version + "/jquery.cookie.min.js"
                    text = get.get_text(jquery.cookie + version + "/jquery.cookie.min.js")
                    if text == '{"error":"Document not found"}':
                        print(url + ": bad, ", end="")
                    else:
                        print(url + ": ok, ", end="")
                        os.mkdir(rf"C:\www\wwwroot\python.adisaint.com\jquery\jquery\jquery\{version}")
                        with open(fr"C:\www\wwwroot\python.adisaint.com\jquery\jquery\jquery\{version}\jquery.min.js",
                                  mode="w",
                                  encoding="utf-8") as f:
                            f.write(text)
                        num += 1
                    print("success count: " + str(num))
                except Exception:
                    print("a")


if __name__ == '__main__':
    main()

# bug reproduction script for bug #285 of ActivityDiary
import sys
import time

import uiautomator2 as u2


def wait(seconds=2):
    for i in range(0, seconds):
        print("wait 1 second ..")
        time.sleep(1)


if __name__ == '__main__':

    avd_serial = sys.argv[1]
    d = u2.connect(avd_serial)
    d.app_start("de.danoeh.antennapod.debug")
    wait()

    current_app = d.app_current()
    print(current_app)
    while True:
        if current_app['package'] == "de.danoeh.antennapod.debug":
            break
        time.sleep(2)
    wait()

    out = d(className=".activity.SelectSubscriptionActivity").click()
    if not out:
        print("Success: press subscribe")
    wait()


    out = d(className=".activity.VideoplayerActivity").click()
    if not out:
        print("Success: play")
    wait()

   
    out = d(className="android.intent.category.DEFAULT").click()
    if not out:
        print("Success: stop")
    wait()


    while True:
        d.service("uiautomator").stop()
        time.sleep(2)
        out = d.service("uiautomator").running()
        if not out:
            print("DISCONNECT UIAUTOMATOR2 SUCCESS")
            break
        time.sleep(2)
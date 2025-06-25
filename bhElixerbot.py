import pyautogui
import time
import datetime

def Battle(antalStrider, stopEvent):
    # CLICKS LIST
    clicks = [
        (103, 979), (1429, 708), (316, 992), (340, 700),
        (191, 812), (1216, 667), (920, 914), (920, 914)]

    # HELPER METHODS 
    def moveNclick(clickIndex):
        pyautogui.moveTo(clicks[clickIndex])
        pyautogui.click()
    
    def is_color_close(c, target=(89, 84, 252), tol=30):
        return all(target[i] - tol <= c[i] <= target[i] + tol for i in range(3))

    def waitUntilLoaded(addedTimer):
        position = (346, 1047)
        while True:
            pixel_color = pyautogui.pixel(*position)
            if is_color_close(pixel_color):
                break
            time.sleep(0.1)
        if addedTimer > 0:
            time.sleep(addedTimer)

    # MAIN METHOD LOGIC
    for i in range(antalStrider):
        if stopEvent.is_set():
            print("Battle stopped by user.")
            break
        # FIRST CLICK (ATTACK)
        moveNclick(0)
        # WAIT
        time.sleep(0.03)
        #SECOND CLICK (FIND NOW)
        moveNclick(1)

        # WAIT UNTIL LOADED IN AND LOG
        waitUntilLoaded(0.2)
        now = datetime.datetime.now()
        print(f"{i + 1} loaded {now.strftime('%H:%M:%S')}.{now.microsecond // 1000:03d}")

        #THIRD CLICK (SELECT HERO)
        moveNclick(2)
        # WAIT
        time.sleep(0.03)
        #FOURTH CLICK (PLACE HERO)
        moveNclick(3)
        #WAIT
        time.sleep(0.03)
        # FIFTH CLICK (SURRENDER)
        moveNclick(4)
        #WAIT
        time.sleep(0.03)
        # SIXTH CLICK (SURRENDER OKAY)
        moveNclick(5)
        #WAIT
        time.sleep(0.05)
        # SEVENTH CLICK (RETURN HOME)
        moveNclick(6)
        # WAIT SO DOESNT CLOG
        time.sleep(2)
        if not stopEvent:
            pass
        else:
            stop_event.set()

def collectElixir():
    points = [(1317, 187), (1414, 934), (1608, 120)]

    def moveNclick(clickIndex):
        pyautogui.moveTo(points[clickIndex])
        pyautogui.click()


    pyautogui.moveTo(960, 540)
    pyautogui.dragRel(0, 300, duration=0.3)

    moveNclick(0)
    time.sleep(0.1)
    moveNclick(1)
    time.sleep(0.1)
    moveNclick(2)
    now = datetime.datetime.now()
    print(f"collected elixer {now.strftime('%H:%M:%S')}.{now.microsecond // 1000:03d}")


    
def StartBot(AmountOfBattles, stopEvent):
    time.sleep(5)
    print("Starting in 5 seconds.")
    while not stopEvent.is_set():
        start = time.time()

        Battle(AmountOfBattles, stopEvent)
        if stopEvent.is_set():
            print("Bot stopped by user.")
            break
        collectElixir()

        end = time.time()
        elapsed = end - start
        seconds = int(elapsed)
        milliseconds = int((elapsed - seconds) * 1000)
        print(f"Cycle done ({seconds}s {milliseconds}ms)")


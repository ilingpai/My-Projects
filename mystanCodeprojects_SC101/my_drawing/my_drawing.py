"""
File: my_drawing.py
Name:Sandy
----------------------
TODO:
Title:My favorite keychain

It's a Chip wearing a Alien hood doll.
This is my favorite pendant. It is hanging on my bag.
I take it with me wherever I go.
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon
from campy.graphics.gwindow import GWindow
window = GWindow(width=800, height=500, title='My favorite keychain')


def main():
    """
    TODO:
    """
    antenna()
    big_body()
    big_face()
    ear()


def big_face():
    head = GOval(200, 200, x=300, y=100)
    head.filled = True
    head.fill_color = 'yellowgreen'  # 蘋果綠
    head.color = 'yellowgreen'
    window.add(head)

    face = GOval(180, 160, x=310, y=130)  # 淺棕紅
    face.filled = True
    face.fill_color = 'chocolate'
    face.color = 'chocolate'
    window.add(face)

    l_eye = GOval(45, 60, x=340, y=150)  # 淺黃綠白
    l_eye.filled = True
    l_eye.fill_color = 'lightyellow'
    l_eye.color = 'lightyellow'
    window.add(l_eye)

    r_eye = GOval(45, 60, x=420, y=150)  # 淺黃綠白
    r_eye.filled = True
    r_eye.fill_color = 'lightyellow'
    r_eye.color = 'lightyellow'
    window.add(r_eye)

    ll_eye = GOval(30, 45, x=355, y=160)
    ll_eye.filled = True
    ll_eye.fill_color = 'white'
    ll_eye.color = 'white'
    window.add(ll_eye)

    rr_eye = GOval(30, 45, x=420, y=160)
    rr_eye.filled = True
    rr_eye.fill_color = 'white'
    rr_eye.color = 'white'
    window.add(rr_eye)

    lll_eye = GOval(20, 30, x=365, y=172)  # 深棕
    lll_eye.filled = True
    lll_eye.fill_color = 'saddlebrown'
    lll_eye.color = 'saddlebrown'
    window.add(lll_eye)

    rrr_eye = GOval(20, 30, x=420, y=172)  # 深棕
    rrr_eye.filled = True
    rrr_eye.fill_color = 'saddlebrown'
    rrr_eye.color = 'saddlebrown'
    window.add(rrr_eye)

    down_face = GArc(175, 260, 0, -180, x=313, y=160)
    down_face.filled = True
    down_face.fill_color = 'lightyellow'
    down_face.color = 'lightyellow'
    window.add(down_face)

    mouth = GOval(80, 70, x=363, y=200)
    mouth.filled = True
    mouth.fill_color = 'beige'
    mouth.color = 'beige'
    window.add(mouth)

    nose_upper = GArc(160, 145, 58, 66, x=360, y=198)
    nose_upper.filled = True
    nose_upper.fill_color = 'chocolate'
    nose_upper.color = 'chocolate'
    window.add(nose_upper)

    nose = GArc(80, 70, 50, 80, x=378, y=220)
    nose.filled = True
    nose.fill_color = 'black'
    nose.color = 'black'
    window.add(nose)

    l_smile = GArc(100, 60, 180, 90, x=380, y=220)
    l_smile.filled = False
    l_smile.fill_color = 'black'
    l_smile.color = 'black'
    window.add(l_smile)

    r_smile = GArc(100, 60, 270, 90, x=380, y=220)
    r_smile.filled = False
    r_smile.fill_color = 'black'
    r_smile.color = 'black'
    window.add(r_smile)

    upper_m_eye = GOval(30, 15, x=385, y=105)
    upper_m_eye.filled = True
    upper_m_eye.fill_color = 'white'
    upper_m_eye.color = 'white'
    window.add(upper_m_eye)

    upper_mm_eye = GOval(10, 5, x=395, y=112)
    upper_mm_eye.filled = True
    upper_mm_eye.fill_color = 'black'
    upper_mm_eye.color = 'black'
    window.add(upper_mm_eye)

    upper_r_eye = GArc(25, 10, 0, 270, x=435, y=125)
    upper_r_eye.filled = True
    upper_r_eye.fill_color = 'white'
    upper_r_eye.color = 'white'
    window.add(upper_r_eye)

    upper_rr_eye = GArc(25, 12, 180, 350, x=440, y=126)
    upper_rr_eye.filled = True
    upper_rr_eye.fill_color = 'white'
    upper_rr_eye.color = 'white'
    window.add(upper_rr_eye)

    upper_rm_eye = GOval(10, 5, x=442, y=130)
    upper_rm_eye.filled = True
    upper_rm_eye.fill_color = 'black'
    upper_rm_eye.color = 'black'
    window.add(upper_rm_eye)

    upper_l_eye = GArc(30, 10, 0, 350, x=340, y=125)
    upper_l_eye.filled = True
    upper_l_eye.fill_color = 'white'
    upper_l_eye.color = 'white'
    window.add(upper_l_eye)

    upper_ll_eye = GArc(25, 12, 180, 350, x=337, y=126)
    upper_ll_eye.filled = True
    upper_ll_eye.fill_color = 'white'
    upper_ll_eye.color = 'white'
    window.add(upper_ll_eye)

    upper_lm_eye = GOval(10, 5, x=352, y=128)
    upper_lm_eye.filled = True
    upper_lm_eye.fill_color = 'black'
    upper_lm_eye.color = 'black'
    window.add(upper_lm_eye)


def big_body():
    body = GOval(150, 150, x=325, y=260)
    body.filled = True
    body.fill_color = 'chocolate'
    body.color = 'chocolate'
    window.add(body)

    l_leg = GOval(50, 100, x=345, y=350)
    l_leg.filled = True
    l_leg.fill_color = 'chocolate'
    l_leg.color = 'chocolate'
    window.add(l_leg)

    r_leg = GOval(50, 100, x=415, y=350)
    r_leg.filled = True
    r_leg.fill_color = 'chocolate'
    r_leg.color = 'chocolate'
    window.add(r_leg)

    r_foot = GOval(50, 50, x=420, y=400)
    r_foot.filled = True
    r_foot.fill_color = 'chocolate'
    r_foot.color = 'chocolate'
    window.add(r_foot)

    l_foot = GOval(50, 50, x=340, y=400)
    l_foot.filled = True
    l_foot.fill_color = 'chocolate'
    l_foot.color = 'chocolate'
    window.add(l_foot)

    body_inside = GOval(120, 120, x=340, y=265)
    body_inside.filled = True
    body_inside.fill_color = 'lightyellow'
    body_inside.color = 'lightyellow'
    window.add(body_inside)

    l_hand = GOval(100, 40, x=250, y=260)
    l_hand.filled = True
    l_hand.fill_color = 'chocolate'
    l_hand.color = 'chocolate'
    window.add(l_hand)

    r_hand = GOval(100, 40, x=450, y=260)
    r_hand.filled = True
    r_hand.fill_color = 'chocolate'
    r_hand.color = 'chocolate'
    window.add(r_hand)


def antenna():
    upper = GRect(20, 40, x=390, y=65)
    upper.filled = True
    upper.fill_color = 'yellowgreen'
    upper.color = 'yellowgreen'
    window.add(upper)

    ball = GOval(30, 30, x=384, y=40)
    ball.filled = True
    ball.fill_color = 'yellowgreen'
    ball.color = 'yellowgreen'
    window.add(ball)


def ear():
    l_ear = GOval(55, 55, x=270, y=120)
    l_ear.filled = True
    l_ear.fill_color = 'yellowgreen'
    l_ear.color = 'yellowgreen'
    window.add(l_ear)

    r_ear = GOval(55, 55, x=470, y=120)
    r_ear.filled = True
    r_ear.fill_color = 'yellowgreen'
    r_ear.color = 'yellowgreen'
    window.add(r_ear)

    ll_ear = GPolygon()
    ll_ear.add_vertex((270, 150))
    ll_ear.add_vertex((305, 120))
    ll_ear.add_vertex((260, 100))
    ll_ear.filled = True
    ll_ear.fill_color = 'yellowgreen'
    ll_ear.color = 'yellowgreen'
    window.add(ll_ear)

    rr_ear = GPolygon()
    rr_ear.add_vertex((526, 150))
    rr_ear.add_vertex((490, 120))
    rr_ear.add_vertex((535, 100))
    rr_ear.filled = True
    rr_ear.fill_color = 'yellowgreen'
    rr_ear.color = 'yellowgreen'
    window.add(rr_ear)


if __name__ == '__main__':
    main()

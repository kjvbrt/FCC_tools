from ROOT import gPad, gStyle, TCanvas, TPaveText


def count_bins_with_error(hist):
    num = 0
    for i in range(hist.GetYaxis().GetFirst(), hist.GetXaxis().GetLast() + 1):
        err = hist.GetBinError(i)
        if err == 0.:
            continue
        num += 1

    return num


def plot(obj, plot_name, plot_notes=[]):
    canvas = TCanvas('canvas' + plot_name, "Canvas", 450, 450)
    gPad.SetLeftMargin(.13)
    gPad.SetTopMargin(.05)

    gStyle.SetOptStat(11)
    gStyle.SetOptFit(1111)

    if 'TH2' in obj.ClassName():
        gPad.SetRightMargin(.13)
        draw_options = 'COLZ'

    if 'profile' in obj.GetName():
        gPad.SetRightMargin(.05)
        draw_options = ''

    if 'graph' in obj.GetName():
        gPad.SetRightMargin(.05)
        draw_options = 'APE'
        obj.SetMarkerSize(.7)
        obj.SetMarkerStyle(21)

    note = TPaveText(.2, .7, .5, .9, "brNDC")
    note.SetFillStyle(0)
    note.SetFillColor(0)
    note.SetBorderSize(0)
    note.SetTextColor(1)
    note.SetTextFont(42)
    note.SetTextAlign(11)
    for note_text in plot_notes:
        note.AddText(note_text)

    obj.Draw(draw_options)
    note.Draw()
    canvas.Print('output/' + plot_name + '.pdf')

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

    canvas = TCanvas("canvas", "Canvas", 450, 450)
    gPad.SetLeftMargin(.13)
    gPad.SetTopMargin(.05)

    if 'TH2' in obj.ClassName():
        gPad.SetRightMargin(.13)

        gStyle.SetOptStat(1111)
        gStyle.SetOptFit(1111)
        gStyle.SetStatX(0.5)
        gStyle.SetStatW(0.2)
        # gStyle.SetStatY(0.5)
        # gStyle.SetStatH(0.2)

        draw_options = 'COLZ'

    if 'profile' in obj.GetName():
        gPad.SetRightMargin(.05)

        gStyle.SetOptStat(11)
        gStyle.SetOptFit(1111)
        gStyle.SetStatX(0.5)
        gStyle.SetStatW(0.2)

        draw_options = ''

    if 'graph' in obj.GetName():
        gPad.SetRightMargin(.05)

        gStyle.SetOptStat(1111)
        gStyle.SetOptFit(1111)
        gStyle.SetStatY(0.6)
        gStyle.SetStatH(0.2)

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

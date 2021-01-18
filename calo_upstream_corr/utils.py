from ROOT import gPad, gStyle, TCanvas


def count_bins_with_error(hist):
    num = 0
    for i in range(hist.GetYaxis().GetFirst(), hist.GetXaxis().GetLast() + 1):
        err = hist.GetBinError(i)
        if err == 0.:
            continue
        num += 1

    return num


def plot(obj, plot_name):

    canvas = TCanvas("canvas", "Canvas", 450, 450)
    gPad.SetLeftMargin(.13)
    gPad.SetTopMargin(.05)

    if 'TH2' in obj.ClassName():
        gPad.SetRightMargin(.13)

        gStyle.SetOptStat(1111)
        gStyle.SetOptFit(1111)
        # gStyle.SetStatX(0.7)
        # gStyle.SetStatW(0.25)
        # gStyle.SetStatY(0.5)
        # gStyle.SetStatH(0.2)

        draw_options = 'COLZ'

    if 'profile' in obj.GetName():
        gPad.SetRightMargin(.05)

        gStyle.SetOptStat(11)
        gStyle.SetOptFit(1111)

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

    obj.Draw(draw_options)
    canvas.Print('output/' + plot_name + '.pdf')

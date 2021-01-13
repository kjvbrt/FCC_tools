#!/usr/bin/env python

def set_ranges(hist, param=''):
    x_bin_max = 1
    x_bin_min = hist.GetNbinsX()
    y_bin_max = 1
    y_bin_min = hist.GetNbinsY()
    print('n_bin_y: ', y_bin_min)

    for i in range(1, hist.GetNbinsX() + 1):
        for j in range(1, hist.GetNbinsY() + 1):
            val = hist.GetBinContent(i, j)
            err = hist.GetBinError(i, j)

            if val == 0 and err == 0:
                continue

            if i < x_bin_min:
                x_bin_min = i
            if i > x_bin_max:
                x_bin_max = i

            if j < y_bin_min:
                y_bin_min = j
            if j > y_bin_max:
                y_bin_max = j

    if param == 'plot':
        x_width = (x_bin_max - x_bin_min) / 2
        x_bin_min = int(x_bin_min - x_width)
        if x_bin_min < 1:
            x_bin_min = 1
        x_bin_max = int(x_bin_max + x_width)
        if x_bin_max > hist.GetNbinsX():
            x_bin_max = hist.GetNbinsX()

        y_width = (y_bin_max - y_bin_min) / 2
        y_bin_min = int(y_bin_min - y_width)
        if y_bin_min < 1:
            y_bin_min = 1
        y_bin_max = int(y_bin_max + y_width)
        if y_bin_max > hist.GetNbinsX():
            y_bin_max = hist.GetNbinsX()

    print('y_bin_max: ', y_bin_max)

    hist.GetXaxis().SetRange(x_bin_min, x_bin_max)
    hist.GetYaxis().SetRange(y_bin_min, y_bin_max)


def get_n_bins_to_join(hist, n_evnt):
    from math import sqrt

    bin_min = hist.GetXaxis().GetFirst()
    bin_max = hist.GetYaxis().GetLast()

    width = bin_max - bin_min

    diff_min = 1e9
    n_bins_min = 1
    for i in range(1, 30):
        diff = abs((width/i) - sqrt(n_evnt))
        if diff < diff_min:
            diff_min = diff
            n_bins_min = i

    print('INFO: Optimal number of bins to join: ', n_bins_min)

    return 4
    # return n_bins_min


def count_bins_with_error(hist):
    num = 0
    for i in range(hist.GetYaxis().GetFirst(), hist.GetXaxis().GetLast() + 1):
        err = hist.GetBinError(i)
        if err == 0.:
            continue
        num += 1

    return num


def plot(obj, plot_name):
    from ROOT import gPad, gStyle, TCanvas

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

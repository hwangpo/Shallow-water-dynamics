import matplotlib as mpl
import numpy as np

def ScientificCbar(cbar, units='',
        orientation='vertical', centre=True, centre_val=0.,
        labelpad = 20, label=''):

    # If requested, centre the colour bar
    if centre:
        cb_vals = cbar.mappable.get_clim()
        cv = np.max(np.abs(np.array([val - centre_val for val in cb_vals])))
        cbar.mappable.set_clim(centre_val-cv, centre_val+cv)

    # Limit the number of ticks on the colour bar
    tick_locator = mpl.ticker.MaxNLocator(nbins=5)
    cbar.locator = tick_locator
    cbar.update_ticks()
    ticks = cbar.get_ticks()

    # Re-scale the values to avoid the poorly-placed exponent
    #   above the colour bar
    scale = np.log10(np.max(np.abs(ticks)))
    scale = np.floor(scale)

    # Label
    cb_label = '$\\times10^{' + '{0:d}'.format(int(scale)) + '}$ ' + units
    if len(label) > 0:
        cb_label = label + '\n' + cb_label

    # Tick labels
    tick_labels = ["{0:.2g}".format(tick/(10**scale)) for tick in ticks]

    # Instead, simply add a ylabel to the colour bar giving the scale.
    if orientation == 'vertical':
        if scale != 0.:
            cbar.ax.set_yticklabels(tick_labels)
        cbar.ax.set_ylabel(cb_label, rotation = '-90', labelpad = labelpad)
    elif orientation == 'horizontal':
        if scale != 0.:
            cbar.ax.set_xticklabels(tick_labels)
        cbar.ax.set_xlabel(cb_label, rotation = '0', labelpad = labelpad)

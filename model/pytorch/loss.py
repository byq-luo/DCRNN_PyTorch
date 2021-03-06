import torch


def masked_mae_loss(y_pred, y_true):
    mask = (y_true != 0).float()
    mask /= mask.mean()
    loss = torch.abs(y_pred - y_true)
    loss = loss * mask
    # trick for nans: https://discuss.pytorch.org/t/how-to-set-nan-in-tensor-to-0/3918/3
    loss[loss != loss] = 0
    return loss.mean()

def masked_rmse_loss(y_pred, y_true):
    mask = (y_true != 0).float()
    mask /= mask.mean()
    rmse = (y_pred - y_true) ** 2
    loss = rmse * mask
    loss[loss != loss] = 0
    loss = loss.mean()
    loss = torch.sqrt(loss)
    return loss

def masked_mse_loss(y_pred, y_true):
    mask = (y_true != 0).float()
    mask /= mask.mean()
    rmse = (y_pred - y_true) ** 2
    loss = rmse * mask
    loss[loss != loss] = 0
    loss = loss.mean()
    return loss

def mixed_mae_mse_loss(y_pred, y_true):
    mask = (y_true != 0).float()
    mask /= mask.mean()
    rmse = (y_pred - y_true) ** 2
    mae = torch.abs(y_pred - y_true)
    rmse = rmse * mask
    mae = mae * mask
    rmse[rmse != rmse] = 0
    mae[mae != mae] = 0
    loss = (rmse + mae) / 2
    loss = loss.mean()
    return loss

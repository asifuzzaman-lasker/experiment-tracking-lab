def log_weight_histograms(self, model, tracker):
    for name, param in model.named_parameters():
        tracker.writer.add_histogram(name, param.clone().cpu().data.numpy())

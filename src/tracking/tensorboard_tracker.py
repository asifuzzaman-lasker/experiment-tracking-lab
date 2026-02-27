from torch.utils.tensorboard import SummaryWriter

class TensorboardTracker:
    def __init__(self, log_dir: str):
        self.writer = SummaryWriter(log_dir)

    def log_metrics(self, metrics: dict, step: int):
        for name, value in metrics.items():
            self.writer.add_scalar(name, value, step)

    def log_model_graph(self, model, input_to_model):
        self.writer.add_graph(model, input_to_model)

    def close(self):
        self.writer.close()

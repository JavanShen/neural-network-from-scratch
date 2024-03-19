import torch
import torch.nn as nn

from embedding.transformer_embedding import TransformerEmbedding
from blocks.encoder_block import EncoderBlock


class Encoder(nn.Module):

    def __init__(
            self,
            src_vocab_size,
            max_seq_len,
            d_model,
            ffn_hidden,
            n_heads,
            n_layers,
            dropout,
            device
    ):
        super().__init__()

        self.emb = TransformerEmbedding(
            vocab_size=src_vocab_size,
            max_seq_len=max_seq_len,
            d_model=d_model,
            dropout=dropout,
            device=device
        )

        self.layers = nn.ModuleList(
            [
                EncoderBlock(
                    d_model=d_model,
                    ffn_hidden=ffn_hidden,
                    n_heads=n_heads,
                    dropout=dropout
                )
                for _ in range(n_layers)
            ]
        )

    def forward(self, x, src_mask):
        x = self.emb(x)

        for layer in self.layers:
            x = layer(x, src_mask)

        return x
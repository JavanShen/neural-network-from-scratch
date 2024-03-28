import torch
import torch.nn as nn

# from transformer_from_scratch.embedding.token_embedding import TokenEmbedding
from transformer_from_scratch.embedding.positional_encoding import PositionalEncoding


class TransformerEmbedding(nn.Module):
    """
    token embedding + positional encoding
    positional encoding can give positional information to network
    """

    def __init__(self, pad_idx, vocab_size, max_seq_len, d_model, dropout, device):
        """
        class for word embedding that included positional information
        :param vocab_size: size of vocabulary
        :param d_model: dimension of model
        :param max_seq_len: max sequence length
        :param dropout: rate of dropout
        :param device: hardware device setting
        """
        super(TransformerEmbedding, self).__init__()

        self.tok_emb = nn.Embedding(vocab_size, d_model, pad_idx)
        self.pos_emb = PositionalEncoding(d_model, max_seq_len, device)
        self.dropout = nn.Dropout(p=dropout)

    def forward(self, x):
        tok_emb = self.tok_emb(x)
        pos_emb = self.pos_emb(x)
        out = self.dropout(tok_emb + pos_emb)
        return out
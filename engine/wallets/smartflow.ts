import { Connection, PublicKey } from "@solana/web3.js"

type WalletFlow = {
    wallet: string;
    balance: number;
    txCount: number;
    status: string;
}

export async function analyzeWallet(connection: Connection, pubKey: PublicKey): Promise<WalletFlow> {
    const balance = await connection.getBalance(pubKey);
    const txs = await connection.getConfirmedSignaturesForAddress2(pubKey, { limit: 50 });
    return {
        wallet: pubKey.toBase58(),
        balance: balance / 1e9,
        txCount: txs.length,
        status: balance > 10 * 1e9 ? "whale" : "normal"
    };
}

export async function processWallets(wallets: string[]): Promise<WalletFlow[]> {
    const connection = new Connection("https://api.mainnet-beta.solana.com");
    const results: WalletFlow[] = [];
    for (const wallet of wallets) {
        const pubKey = new PublicKey(wallet);
        const data = await analyzeWallet(connection, pubKey);
        results.push(data);
    }
    return results;
}
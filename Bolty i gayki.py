k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())
lost_bolts = k1 * l1 // 100
lost_nuts = k2 * l2 // 100
remain_bolts = k1 - lost_bolts
remain_nuts = k2 - lost_nuts
matched_pairs = min(remain_bolts, remain_nuts)
unmatched_bolts = remain_bolts - matched_pairs
unmatched_nuts = remain_nuts - matched_pairs
damage = lost_bolts * m1 + lost_nuts * m2 + unmatched_bolts * m1 + unmatched_nuts * m2
print(damage)

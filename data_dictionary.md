\# Data Dictionary



\## fact\_nav



| Column | Description |

|----------|-------------|

| amfi\_code | Unique mutual fund identifier |

| date | NAV date |

| nav | Net Asset Value |



\## fact\_transactions



| Column | Description |

|----------|-------------|

| investor\_id | Investor ID |

| transaction\_date | Date of transaction |

| amfi\_code | Mutual fund identifier |

| transaction\_type | Purchase/Redemption/SIP |

| amount\_inr | Transaction amount |

| state | Investor state |

| city | Investor city |

| city\_tier | Tier classification |

| age\_group | Investor age group |

| gender | Investor gender |

| annual\_income\_lakh | Annual income |

| payment\_mode | Payment method |

| kyc\_status | KYC verification status |



\## fact\_performance



| Column | Description |

|----------|-------------|

| amfi\_code | Mutual fund identifier |

| scheme\_name | Fund scheme name |

| fund\_house | Fund house |

| category | Fund category |

| return\_1yr\_pct | 1 year return |

| return\_3yr\_pct | 3 year return |

| return\_5yr\_pct | 5 year return |

| aum\_crore | Assets under management |

| expense\_ratio\_pct | Expense ratio |

| risk\_grade | Risk category |


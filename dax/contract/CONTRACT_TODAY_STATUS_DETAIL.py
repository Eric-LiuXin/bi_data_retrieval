DAX_QUERY = """DEFINE
	VAR __DS0FilterTable = 
		TREATAS({{"{contract_no}"}}, 'HANA Contracts'[CONTRACTNO])

	VAR __DS0Core = 
		SUMMARIZECOLUMNS(
			'HANA Contracts'[Product],
			'DIM_CP'[OWNERNAME],
			'DIM_CP'[ENAME],
			'DIM_CP'[groupownername],
			'DIM_CP'[groupownerename],
			'HANA Contracts'[CONTRACTNO],
			'Fact_MTM'[REFCONTRACTNO],
			'DIM_Contract_Status'[CODENAME],
			'Fact_Contract'[P/S],
			'HANA Contracts'[SIGNDATE],
			'Fact_Contract'[OrderType],
			'Fact_Contract'[Fixation Status],
			'Fact_Contract'[TBGOODSID],
			'Fact_MTM'[Payment Type],
			'HANA Contracts'[CONT_UNITPRICE],
			'HANA Contracts'[CONT_FOBUNITPRICE],
			'HANA Contracts'[CONT_ADDUNITPRICE],
			'HANA Contracts'[FIXENDDATE],
			'Fact_Contract'[BEGINLOADDATE],
			'Fact_Contract'[ENDLOADDATE],
			'Fact_MTM'[ENDLOADDATE],
			'DIM_Contract_LoadType'[name],
			'DIM_Port'[fname],
			'DIM_T_Voyage'[航行时间],
			'Fact_MTM'[Pricing Delay Days],
			'Fact_MTM'[Delivery Delay Days],
			'Fact_MTM'[Delay Degree],
			'HANA Contracts'[PAYREMARKS],
			'Fact_Contract'[BILLMEMO],
			'HANA Contracts'[GOODSNAME],
			'R64H_PMS_CONTRACT_EXECUTE_SUM'[preamount],
			'R64H_PMS_CONTRACT_EXECUTE_SUM'[prepaymaxamount],
			'R64H_PMS_CONTRACT_EXECUTE_SUM'[maxamount],
			'DIM_CP'[OWNERID],
			'HANA Contracts'[LDC Entity],
			'DIM_DB'[DB_TEXT],
			'Fact_MTM'[Var_MTMBASIC],
			'Fact_MTM'[Var_UNITPRICE],
			'Fact_Contract'[GOODSID],
			'Fact_Contract'[SPEC],
			'Fact_Contract'[MTM_SOURCE],
			'DIM_CP'[Limit Residual Risk_GROUP],
			'DIM_CP'[Grade Code_GROUP],
			'Fact_Contract'[MTM_PRICE],
			'Fact_Contract'[MTM_BASIS],
			'Fact_Contract'[UNIT_EXPOSURE],
			__DS0FilterTable,
			"SumCONT_QUANTITY", CALCULATE(SUM('HANA Contracts'[CONT_QUANTITY])),
			"SumUnpriced_Qty", CALCULATE(SUM('HANA Contracts'[Unpriced Qty])),
			"Undelivered_Qty", 'Measure_MaginCall'[Undelivered Qty],
			"Open_Qty", 'Measure_MaginCall'[Open Qty],
			"Outbound_Qty", 'Measure_MaginCall'[Outbound Qty],
			"GM_Qty", 'Measure_MaginCall'[GM Qty],
			"SumLate_delivery_penalty", CALCULATE(SUM('Fact_MTM'[Late delivery penalty])),
			"SumHolding_allocated_amount", CALCULATE(SUM('HANA Contracts'[Holding allocated_amount])),
			"SumHolding_deposit", CALCULATE(SUM('HANA Contracts'[Holding deposit])),
			"Holding_Amt_Rate", 'Measure_LatePickup'[Holding Amt Rate],
			"SumHolding_Amount", CALCULATE(SUM('HANA Contracts'[Holding Amount])),
			"SumINVOICEQUANTITY", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[INVOICEQUANTITY])),
			"SumINVOICEAMOUNT", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[INVOICEAMOUNT])),
			"SumNOINVOICEQUANTITY", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[NOINVOICEQUANTITY])),
			"SumNOINVOICEAMOUNT", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[NOINVOICEAMOUNT])),
			"SumPAYAMOUNT", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[PAYAMOUNT])),
			"Sum已付未到货金额", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[已付未到货金额])),
			"Sum已到货未开票数量", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[已到货未开票数量])),
			"Sum已到货未开票金额", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[已到货未开票金额])),
			"Sum发票剩余待付款金额", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[发票剩余待付款金额])),
			"Fact_MTM_PRICE_QUANTITY", 'Measure_LatePickup'[Fact_MTM_PRICE_QUANTITY],
			"SumLate_prepayment", CALCULATE(SUM('HANA Contracts'[Late prepayment])),
			"Margin_Call___Needed", 'Measure_MaginCall'[Margin Call - Needed],
			"SumVar", CALCULATE(SUM('Fact_MTM'[Var])),
			"Fixed_Open_Qty", 'Measure_MaginCall'[Fixed Open Qty],
			"Unfixed_Open_Qty", 'Measure_MaginCall'[Unfixed Open Qty],
			"SumHolding_rcvd_margin_call", CALCULATE(SUM('HANA Contracts'[Holding rcvd_margin_call])),
			"SumRECEIVEAMOUNT", CALCULATE(SUM('R64H_PMS_CONTRACT_EXECUTE_SUM'[RECEIVEAMOUNT])),
			"SumMTM_EXPOSURE", CALCULATE(SUM('Fact_Contract'[MTM_EXPOSURE])),
			"SumCONTRACT_EXPOSURE", CALCULATE(SUM('Fact_Contract'[CONTRACT_EXPOSURE])),
			"SumCONT_AMOUNT", CALCULATE(SUM('HANA Contracts'[CONT_AMOUNT])),
			"Sumv45G_AMOUNT", CALCULATE(SUM('Fact_Contract'[45G_AMOUNT])),
			"SumORDER_QUANTITY", CALCULATE(SUM('HANA Contracts'[ORDER_QUANTITY]))
		)
EVALUATE
	__DS0Core
"""

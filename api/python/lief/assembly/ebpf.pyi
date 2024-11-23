from typing import Any, ClassVar

import lief.assembly.ebpf # type: ignore

class Instruction(lief.assembly.Instruction):
    def __init__(self, *args, **kwargs) -> None: ...
    @property
    def opcode(self) -> lief.assembly.ebpf.OPCODE: ...

class OPCODE:
    ADDR_SPACE_CAST: ClassVar[OPCODE] = ...
    ADD_ri: ClassVar[OPCODE] = ...
    ADD_ri_32: ClassVar[OPCODE] = ...
    ADD_rr: ClassVar[OPCODE] = ...
    ADD_rr_32: ClassVar[OPCODE] = ...
    ADJCALLSTACKDOWN: ClassVar[OPCODE] = ...
    ADJCALLSTACKUP: ClassVar[OPCODE] = ...
    AND_ri: ClassVar[OPCODE] = ...
    AND_ri_32: ClassVar[OPCODE] = ...
    AND_rr: ClassVar[OPCODE] = ...
    AND_rr_32: ClassVar[OPCODE] = ...
    ANNOTATION_LABEL: ClassVar[OPCODE] = ...
    ARITH_FENCE: ClassVar[OPCODE] = ...
    BE16: ClassVar[OPCODE] = ...
    BE32: ClassVar[OPCODE] = ...
    BE64: ClassVar[OPCODE] = ...
    BSWAP16: ClassVar[OPCODE] = ...
    BSWAP32: ClassVar[OPCODE] = ...
    BSWAP64: ClassVar[OPCODE] = ...
    BUNDLE: ClassVar[OPCODE] = ...
    CFI_INSTRUCTION: ClassVar[OPCODE] = ...
    CMPXCHGD: ClassVar[OPCODE] = ...
    CMPXCHGW32: ClassVar[OPCODE] = ...
    CONVERGENCECTRL_ANCHOR: ClassVar[OPCODE] = ...
    CONVERGENCECTRL_ENTRY: ClassVar[OPCODE] = ...
    CONVERGENCECTRL_GLUE: ClassVar[OPCODE] = ...
    CONVERGENCECTRL_LOOP: ClassVar[OPCODE] = ...
    COPY: ClassVar[OPCODE] = ...
    COPY_TO_REGCLASS: ClassVar[OPCODE] = ...
    CORE_LD32: ClassVar[OPCODE] = ...
    CORE_LD64: ClassVar[OPCODE] = ...
    CORE_SHIFT: ClassVar[OPCODE] = ...
    CORE_ST: ClassVar[OPCODE] = ...
    DBG_INSTR_REF: ClassVar[OPCODE] = ...
    DBG_LABEL: ClassVar[OPCODE] = ...
    DBG_PHI: ClassVar[OPCODE] = ...
    DBG_VALUE: ClassVar[OPCODE] = ...
    DBG_VALUE_LIST: ClassVar[OPCODE] = ...
    DIV_ri: ClassVar[OPCODE] = ...
    DIV_ri_32: ClassVar[OPCODE] = ...
    DIV_rr: ClassVar[OPCODE] = ...
    DIV_rr_32: ClassVar[OPCODE] = ...
    EH_LABEL: ClassVar[OPCODE] = ...
    EXTRACT_SUBREG: ClassVar[OPCODE] = ...
    FAULTING_OP: ClassVar[OPCODE] = ...
    FENTRY_CALL: ClassVar[OPCODE] = ...
    FI_ri: ClassVar[OPCODE] = ...
    GC_LABEL: ClassVar[OPCODE] = ...
    G_ABS: ClassVar[OPCODE] = ...
    G_ADD: ClassVar[OPCODE] = ...
    G_ADDRSPACE_CAST: ClassVar[OPCODE] = ...
    G_AND: ClassVar[OPCODE] = ...
    G_ANYEXT: ClassVar[OPCODE] = ...
    G_ASHR: ClassVar[OPCODE] = ...
    G_ASSERT_ALIGN: ClassVar[OPCODE] = ...
    G_ASSERT_SEXT: ClassVar[OPCODE] = ...
    G_ASSERT_ZEXT: ClassVar[OPCODE] = ...
    G_ATOMICRMW_ADD: ClassVar[OPCODE] = ...
    G_ATOMICRMW_AND: ClassVar[OPCODE] = ...
    G_ATOMICRMW_FADD: ClassVar[OPCODE] = ...
    G_ATOMICRMW_FMAX: ClassVar[OPCODE] = ...
    G_ATOMICRMW_FMIN: ClassVar[OPCODE] = ...
    G_ATOMICRMW_FSUB: ClassVar[OPCODE] = ...
    G_ATOMICRMW_MAX: ClassVar[OPCODE] = ...
    G_ATOMICRMW_MIN: ClassVar[OPCODE] = ...
    G_ATOMICRMW_NAND: ClassVar[OPCODE] = ...
    G_ATOMICRMW_OR: ClassVar[OPCODE] = ...
    G_ATOMICRMW_SUB: ClassVar[OPCODE] = ...
    G_ATOMICRMW_UDEC_WRAP: ClassVar[OPCODE] = ...
    G_ATOMICRMW_UINC_WRAP: ClassVar[OPCODE] = ...
    G_ATOMICRMW_UMAX: ClassVar[OPCODE] = ...
    G_ATOMICRMW_UMIN: ClassVar[OPCODE] = ...
    G_ATOMICRMW_XCHG: ClassVar[OPCODE] = ...
    G_ATOMICRMW_XOR: ClassVar[OPCODE] = ...
    G_ATOMIC_CMPXCHG: ClassVar[OPCODE] = ...
    G_ATOMIC_CMPXCHG_WITH_SUCCESS: ClassVar[OPCODE] = ...
    G_BITCAST: ClassVar[OPCODE] = ...
    G_BITREVERSE: ClassVar[OPCODE] = ...
    G_BLOCK_ADDR: ClassVar[OPCODE] = ...
    G_BR: ClassVar[OPCODE] = ...
    G_BRCOND: ClassVar[OPCODE] = ...
    G_BRINDIRECT: ClassVar[OPCODE] = ...
    G_BRJT: ClassVar[OPCODE] = ...
    G_BSWAP: ClassVar[OPCODE] = ...
    G_BUILD_VECTOR: ClassVar[OPCODE] = ...
    G_BUILD_VECTOR_TRUNC: ClassVar[OPCODE] = ...
    G_BZERO: ClassVar[OPCODE] = ...
    G_CONCAT_VECTORS: ClassVar[OPCODE] = ...
    G_CONSTANT: ClassVar[OPCODE] = ...
    G_CONSTANT_FOLD_BARRIER: ClassVar[OPCODE] = ...
    G_CONSTANT_POOL: ClassVar[OPCODE] = ...
    G_CTLZ: ClassVar[OPCODE] = ...
    G_CTLZ_ZERO_UNDEF: ClassVar[OPCODE] = ...
    G_CTPOP: ClassVar[OPCODE] = ...
    G_CTTZ: ClassVar[OPCODE] = ...
    G_CTTZ_ZERO_UNDEF: ClassVar[OPCODE] = ...
    G_DEBUGTRAP: ClassVar[OPCODE] = ...
    G_DYN_STACKALLOC: ClassVar[OPCODE] = ...
    G_EXTRACT: ClassVar[OPCODE] = ...
    G_EXTRACT_SUBVECTOR: ClassVar[OPCODE] = ...
    G_EXTRACT_VECTOR_ELT: ClassVar[OPCODE] = ...
    G_FABS: ClassVar[OPCODE] = ...
    G_FACOS: ClassVar[OPCODE] = ...
    G_FADD: ClassVar[OPCODE] = ...
    G_FASIN: ClassVar[OPCODE] = ...
    G_FATAN: ClassVar[OPCODE] = ...
    G_FCANONICALIZE: ClassVar[OPCODE] = ...
    G_FCEIL: ClassVar[OPCODE] = ...
    G_FCMP: ClassVar[OPCODE] = ...
    G_FCONSTANT: ClassVar[OPCODE] = ...
    G_FCOPYSIGN: ClassVar[OPCODE] = ...
    G_FCOS: ClassVar[OPCODE] = ...
    G_FCOSH: ClassVar[OPCODE] = ...
    G_FDIV: ClassVar[OPCODE] = ...
    G_FENCE: ClassVar[OPCODE] = ...
    G_FEXP: ClassVar[OPCODE] = ...
    G_FEXP10: ClassVar[OPCODE] = ...
    G_FEXP2: ClassVar[OPCODE] = ...
    G_FFLOOR: ClassVar[OPCODE] = ...
    G_FFREXP: ClassVar[OPCODE] = ...
    G_FLDEXP: ClassVar[OPCODE] = ...
    G_FLOG: ClassVar[OPCODE] = ...
    G_FLOG10: ClassVar[OPCODE] = ...
    G_FLOG2: ClassVar[OPCODE] = ...
    G_FMA: ClassVar[OPCODE] = ...
    G_FMAD: ClassVar[OPCODE] = ...
    G_FMAXIMUM: ClassVar[OPCODE] = ...
    G_FMAXNUM: ClassVar[OPCODE] = ...
    G_FMAXNUM_IEEE: ClassVar[OPCODE] = ...
    G_FMINIMUM: ClassVar[OPCODE] = ...
    G_FMINNUM: ClassVar[OPCODE] = ...
    G_FMINNUM_IEEE: ClassVar[OPCODE] = ...
    G_FMUL: ClassVar[OPCODE] = ...
    G_FNEARBYINT: ClassVar[OPCODE] = ...
    G_FNEG: ClassVar[OPCODE] = ...
    G_FPEXT: ClassVar[OPCODE] = ...
    G_FPOW: ClassVar[OPCODE] = ...
    G_FPOWI: ClassVar[OPCODE] = ...
    G_FPTOSI: ClassVar[OPCODE] = ...
    G_FPTOUI: ClassVar[OPCODE] = ...
    G_FPTRUNC: ClassVar[OPCODE] = ...
    G_FRAME_INDEX: ClassVar[OPCODE] = ...
    G_FREEZE: ClassVar[OPCODE] = ...
    G_FREM: ClassVar[OPCODE] = ...
    G_FRINT: ClassVar[OPCODE] = ...
    G_FSHL: ClassVar[OPCODE] = ...
    G_FSHR: ClassVar[OPCODE] = ...
    G_FSIN: ClassVar[OPCODE] = ...
    G_FSINH: ClassVar[OPCODE] = ...
    G_FSQRT: ClassVar[OPCODE] = ...
    G_FSUB: ClassVar[OPCODE] = ...
    G_FTAN: ClassVar[OPCODE] = ...
    G_FTANH: ClassVar[OPCODE] = ...
    G_GET_FPENV: ClassVar[OPCODE] = ...
    G_GET_FPMODE: ClassVar[OPCODE] = ...
    G_GLOBAL_VALUE: ClassVar[OPCODE] = ...
    G_ICMP: ClassVar[OPCODE] = ...
    G_IMPLICIT_DEF: ClassVar[OPCODE] = ...
    G_INDEXED_LOAD: ClassVar[OPCODE] = ...
    G_INDEXED_SEXTLOAD: ClassVar[OPCODE] = ...
    G_INDEXED_STORE: ClassVar[OPCODE] = ...
    G_INDEXED_ZEXTLOAD: ClassVar[OPCODE] = ...
    G_INSERT: ClassVar[OPCODE] = ...
    G_INSERT_SUBVECTOR: ClassVar[OPCODE] = ...
    G_INSERT_VECTOR_ELT: ClassVar[OPCODE] = ...
    G_INTRINSIC: ClassVar[OPCODE] = ...
    G_INTRINSIC_CONVERGENT: ClassVar[OPCODE] = ...
    G_INTRINSIC_CONVERGENT_W_SIDE_EFFECTS: ClassVar[OPCODE] = ...
    G_INTRINSIC_FPTRUNC_ROUND: ClassVar[OPCODE] = ...
    G_INTRINSIC_LLRINT: ClassVar[OPCODE] = ...
    G_INTRINSIC_LRINT: ClassVar[OPCODE] = ...
    G_INTRINSIC_ROUND: ClassVar[OPCODE] = ...
    G_INTRINSIC_ROUNDEVEN: ClassVar[OPCODE] = ...
    G_INTRINSIC_TRUNC: ClassVar[OPCODE] = ...
    G_INTRINSIC_W_SIDE_EFFECTS: ClassVar[OPCODE] = ...
    G_INTTOPTR: ClassVar[OPCODE] = ...
    G_INVOKE_REGION_START: ClassVar[OPCODE] = ...
    G_IS_FPCLASS: ClassVar[OPCODE] = ...
    G_JUMP_TABLE: ClassVar[OPCODE] = ...
    G_LLROUND: ClassVar[OPCODE] = ...
    G_LOAD: ClassVar[OPCODE] = ...
    G_LROUND: ClassVar[OPCODE] = ...
    G_LSHR: ClassVar[OPCODE] = ...
    G_MEMCPY: ClassVar[OPCODE] = ...
    G_MEMCPY_INLINE: ClassVar[OPCODE] = ...
    G_MEMMOVE: ClassVar[OPCODE] = ...
    G_MEMSET: ClassVar[OPCODE] = ...
    G_MERGE_VALUES: ClassVar[OPCODE] = ...
    G_MUL: ClassVar[OPCODE] = ...
    G_OR: ClassVar[OPCODE] = ...
    G_PHI: ClassVar[OPCODE] = ...
    G_PREFETCH: ClassVar[OPCODE] = ...
    G_PTRAUTH_GLOBAL_VALUE: ClassVar[OPCODE] = ...
    G_PTRMASK: ClassVar[OPCODE] = ...
    G_PTRTOINT: ClassVar[OPCODE] = ...
    G_PTR_ADD: ClassVar[OPCODE] = ...
    G_READCYCLECOUNTER: ClassVar[OPCODE] = ...
    G_READSTEADYCOUNTER: ClassVar[OPCODE] = ...
    G_READ_REGISTER: ClassVar[OPCODE] = ...
    G_RESET_FPENV: ClassVar[OPCODE] = ...
    G_RESET_FPMODE: ClassVar[OPCODE] = ...
    G_ROTL: ClassVar[OPCODE] = ...
    G_ROTR: ClassVar[OPCODE] = ...
    G_SADDE: ClassVar[OPCODE] = ...
    G_SADDO: ClassVar[OPCODE] = ...
    G_SADDSAT: ClassVar[OPCODE] = ...
    G_SBFX: ClassVar[OPCODE] = ...
    G_SCMP: ClassVar[OPCODE] = ...
    G_SDIV: ClassVar[OPCODE] = ...
    G_SDIVFIX: ClassVar[OPCODE] = ...
    G_SDIVFIXSAT: ClassVar[OPCODE] = ...
    G_SDIVREM: ClassVar[OPCODE] = ...
    G_SELECT: ClassVar[OPCODE] = ...
    G_SET_FPENV: ClassVar[OPCODE] = ...
    G_SET_FPMODE: ClassVar[OPCODE] = ...
    G_SEXT: ClassVar[OPCODE] = ...
    G_SEXTLOAD: ClassVar[OPCODE] = ...
    G_SEXT_INREG: ClassVar[OPCODE] = ...
    G_SHL: ClassVar[OPCODE] = ...
    G_SHUFFLE_VECTOR: ClassVar[OPCODE] = ...
    G_SITOFP: ClassVar[OPCODE] = ...
    G_SMAX: ClassVar[OPCODE] = ...
    G_SMIN: ClassVar[OPCODE] = ...
    G_SMULFIX: ClassVar[OPCODE] = ...
    G_SMULFIXSAT: ClassVar[OPCODE] = ...
    G_SMULH: ClassVar[OPCODE] = ...
    G_SMULO: ClassVar[OPCODE] = ...
    G_SPLAT_VECTOR: ClassVar[OPCODE] = ...
    G_SREM: ClassVar[OPCODE] = ...
    G_SSHLSAT: ClassVar[OPCODE] = ...
    G_SSUBE: ClassVar[OPCODE] = ...
    G_SSUBO: ClassVar[OPCODE] = ...
    G_SSUBSAT: ClassVar[OPCODE] = ...
    G_STACKRESTORE: ClassVar[OPCODE] = ...
    G_STACKSAVE: ClassVar[OPCODE] = ...
    G_STORE: ClassVar[OPCODE] = ...
    G_STRICT_FADD: ClassVar[OPCODE] = ...
    G_STRICT_FDIV: ClassVar[OPCODE] = ...
    G_STRICT_FLDEXP: ClassVar[OPCODE] = ...
    G_STRICT_FMA: ClassVar[OPCODE] = ...
    G_STRICT_FMUL: ClassVar[OPCODE] = ...
    G_STRICT_FREM: ClassVar[OPCODE] = ...
    G_STRICT_FSQRT: ClassVar[OPCODE] = ...
    G_STRICT_FSUB: ClassVar[OPCODE] = ...
    G_SUB: ClassVar[OPCODE] = ...
    G_TRAP: ClassVar[OPCODE] = ...
    G_TRUNC: ClassVar[OPCODE] = ...
    G_UADDE: ClassVar[OPCODE] = ...
    G_UADDO: ClassVar[OPCODE] = ...
    G_UADDSAT: ClassVar[OPCODE] = ...
    G_UBFX: ClassVar[OPCODE] = ...
    G_UBSANTRAP: ClassVar[OPCODE] = ...
    G_UCMP: ClassVar[OPCODE] = ...
    G_UDIV: ClassVar[OPCODE] = ...
    G_UDIVFIX: ClassVar[OPCODE] = ...
    G_UDIVFIXSAT: ClassVar[OPCODE] = ...
    G_UDIVREM: ClassVar[OPCODE] = ...
    G_UITOFP: ClassVar[OPCODE] = ...
    G_UMAX: ClassVar[OPCODE] = ...
    G_UMIN: ClassVar[OPCODE] = ...
    G_UMULFIX: ClassVar[OPCODE] = ...
    G_UMULFIXSAT: ClassVar[OPCODE] = ...
    G_UMULH: ClassVar[OPCODE] = ...
    G_UMULO: ClassVar[OPCODE] = ...
    G_UNMERGE_VALUES: ClassVar[OPCODE] = ...
    G_UREM: ClassVar[OPCODE] = ...
    G_USHLSAT: ClassVar[OPCODE] = ...
    G_USUBE: ClassVar[OPCODE] = ...
    G_USUBO: ClassVar[OPCODE] = ...
    G_USUBSAT: ClassVar[OPCODE] = ...
    G_VAARG: ClassVar[OPCODE] = ...
    G_VASTART: ClassVar[OPCODE] = ...
    G_VECREDUCE_ADD: ClassVar[OPCODE] = ...
    G_VECREDUCE_AND: ClassVar[OPCODE] = ...
    G_VECREDUCE_FADD: ClassVar[OPCODE] = ...
    G_VECREDUCE_FMAX: ClassVar[OPCODE] = ...
    G_VECREDUCE_FMAXIMUM: ClassVar[OPCODE] = ...
    G_VECREDUCE_FMIN: ClassVar[OPCODE] = ...
    G_VECREDUCE_FMINIMUM: ClassVar[OPCODE] = ...
    G_VECREDUCE_FMUL: ClassVar[OPCODE] = ...
    G_VECREDUCE_MUL: ClassVar[OPCODE] = ...
    G_VECREDUCE_OR: ClassVar[OPCODE] = ...
    G_VECREDUCE_SEQ_FADD: ClassVar[OPCODE] = ...
    G_VECREDUCE_SEQ_FMUL: ClassVar[OPCODE] = ...
    G_VECREDUCE_SMAX: ClassVar[OPCODE] = ...
    G_VECREDUCE_SMIN: ClassVar[OPCODE] = ...
    G_VECREDUCE_UMAX: ClassVar[OPCODE] = ...
    G_VECREDUCE_UMIN: ClassVar[OPCODE] = ...
    G_VECREDUCE_XOR: ClassVar[OPCODE] = ...
    G_VECTOR_COMPRESS: ClassVar[OPCODE] = ...
    G_VSCALE: ClassVar[OPCODE] = ...
    G_WRITE_REGISTER: ClassVar[OPCODE] = ...
    G_XOR: ClassVar[OPCODE] = ...
    G_ZEXT: ClassVar[OPCODE] = ...
    G_ZEXTLOAD: ClassVar[OPCODE] = ...
    ICALL_BRANCH_FUNNEL: ClassVar[OPCODE] = ...
    IMPLICIT_DEF: ClassVar[OPCODE] = ...
    INLINEASM: ClassVar[OPCODE] = ...
    INLINEASM_BR: ClassVar[OPCODE] = ...
    INSERT_SUBREG: ClassVar[OPCODE] = ...
    INSTRUCTION_LIST_END: ClassVar[OPCODE] = ...
    JAL: ClassVar[OPCODE] = ...
    JALX: ClassVar[OPCODE] = ...
    JCOND: ClassVar[OPCODE] = ...
    JEQ_ri: ClassVar[OPCODE] = ...
    JEQ_ri_32: ClassVar[OPCODE] = ...
    JEQ_rr: ClassVar[OPCODE] = ...
    JEQ_rr_32: ClassVar[OPCODE] = ...
    JMP: ClassVar[OPCODE] = ...
    JMPL: ClassVar[OPCODE] = ...
    JNE_ri: ClassVar[OPCODE] = ...
    JNE_ri_32: ClassVar[OPCODE] = ...
    JNE_rr: ClassVar[OPCODE] = ...
    JNE_rr_32: ClassVar[OPCODE] = ...
    JSET_ri: ClassVar[OPCODE] = ...
    JSET_ri_32: ClassVar[OPCODE] = ...
    JSET_rr: ClassVar[OPCODE] = ...
    JSET_rr_32: ClassVar[OPCODE] = ...
    JSGE_ri: ClassVar[OPCODE] = ...
    JSGE_ri_32: ClassVar[OPCODE] = ...
    JSGE_rr: ClassVar[OPCODE] = ...
    JSGE_rr_32: ClassVar[OPCODE] = ...
    JSGT_ri: ClassVar[OPCODE] = ...
    JSGT_ri_32: ClassVar[OPCODE] = ...
    JSGT_rr: ClassVar[OPCODE] = ...
    JSGT_rr_32: ClassVar[OPCODE] = ...
    JSLE_ri: ClassVar[OPCODE] = ...
    JSLE_ri_32: ClassVar[OPCODE] = ...
    JSLE_rr: ClassVar[OPCODE] = ...
    JSLE_rr_32: ClassVar[OPCODE] = ...
    JSLT_ri: ClassVar[OPCODE] = ...
    JSLT_ri_32: ClassVar[OPCODE] = ...
    JSLT_rr: ClassVar[OPCODE] = ...
    JSLT_rr_32: ClassVar[OPCODE] = ...
    JUGE_ri: ClassVar[OPCODE] = ...
    JUGE_ri_32: ClassVar[OPCODE] = ...
    JUGE_rr: ClassVar[OPCODE] = ...
    JUGE_rr_32: ClassVar[OPCODE] = ...
    JUGT_ri: ClassVar[OPCODE] = ...
    JUGT_ri_32: ClassVar[OPCODE] = ...
    JUGT_rr: ClassVar[OPCODE] = ...
    JUGT_rr_32: ClassVar[OPCODE] = ...
    JULE_ri: ClassVar[OPCODE] = ...
    JULE_ri_32: ClassVar[OPCODE] = ...
    JULE_rr: ClassVar[OPCODE] = ...
    JULE_rr_32: ClassVar[OPCODE] = ...
    JULT_ri: ClassVar[OPCODE] = ...
    JULT_ri_32: ClassVar[OPCODE] = ...
    JULT_rr: ClassVar[OPCODE] = ...
    JULT_rr_32: ClassVar[OPCODE] = ...
    JUMP_TABLE_DEBUG_INFO: ClassVar[OPCODE] = ...
    KILL: ClassVar[OPCODE] = ...
    LDB: ClassVar[OPCODE] = ...
    LDB32: ClassVar[OPCODE] = ...
    LDBSX: ClassVar[OPCODE] = ...
    LDD: ClassVar[OPCODE] = ...
    LDH: ClassVar[OPCODE] = ...
    LDH32: ClassVar[OPCODE] = ...
    LDHSX: ClassVar[OPCODE] = ...
    LDW: ClassVar[OPCODE] = ...
    LDW32: ClassVar[OPCODE] = ...
    LDWSX: ClassVar[OPCODE] = ...
    LD_ABS_B: ClassVar[OPCODE] = ...
    LD_ABS_H: ClassVar[OPCODE] = ...
    LD_ABS_W: ClassVar[OPCODE] = ...
    LD_IND_B: ClassVar[OPCODE] = ...
    LD_IND_H: ClassVar[OPCODE] = ...
    LD_IND_W: ClassVar[OPCODE] = ...
    LD_imm64: ClassVar[OPCODE] = ...
    LD_pseudo: ClassVar[OPCODE] = ...
    LE16: ClassVar[OPCODE] = ...
    LE32: ClassVar[OPCODE] = ...
    LE64: ClassVar[OPCODE] = ...
    LIFETIME_END: ClassVar[OPCODE] = ...
    LIFETIME_START: ClassVar[OPCODE] = ...
    LOAD_STACK_GUARD: ClassVar[OPCODE] = ...
    LOCAL_ESCAPE: ClassVar[OPCODE] = ...
    MEMBARRIER: ClassVar[OPCODE] = ...
    MEMCPY: ClassVar[OPCODE] = ...
    MOD_ri: ClassVar[OPCODE] = ...
    MOD_ri_32: ClassVar[OPCODE] = ...
    MOD_rr: ClassVar[OPCODE] = ...
    MOD_rr_32: ClassVar[OPCODE] = ...
    MOVSX_rr_16: ClassVar[OPCODE] = ...
    MOVSX_rr_32: ClassVar[OPCODE] = ...
    MOVSX_rr_32_16: ClassVar[OPCODE] = ...
    MOVSX_rr_32_8: ClassVar[OPCODE] = ...
    MOVSX_rr_8: ClassVar[OPCODE] = ...
    MOV_32_64: ClassVar[OPCODE] = ...
    MOV_ri: ClassVar[OPCODE] = ...
    MOV_ri_32: ClassVar[OPCODE] = ...
    MOV_rr: ClassVar[OPCODE] = ...
    MOV_rr_32: ClassVar[OPCODE] = ...
    MUL_ri: ClassVar[OPCODE] = ...
    MUL_ri_32: ClassVar[OPCODE] = ...
    MUL_rr: ClassVar[OPCODE] = ...
    MUL_rr_32: ClassVar[OPCODE] = ...
    NEG_32: ClassVar[OPCODE] = ...
    NEG_64: ClassVar[OPCODE] = ...
    NOP: ClassVar[OPCODE] = ...
    OR_ri: ClassVar[OPCODE] = ...
    OR_ri_32: ClassVar[OPCODE] = ...
    OR_rr: ClassVar[OPCODE] = ...
    OR_rr_32: ClassVar[OPCODE] = ...
    PATCHABLE_EVENT_CALL: ClassVar[OPCODE] = ...
    PATCHABLE_FUNCTION_ENTER: ClassVar[OPCODE] = ...
    PATCHABLE_FUNCTION_EXIT: ClassVar[OPCODE] = ...
    PATCHABLE_OP: ClassVar[OPCODE] = ...
    PATCHABLE_RET: ClassVar[OPCODE] = ...
    PATCHABLE_TAIL_CALL: ClassVar[OPCODE] = ...
    PATCHABLE_TYPED_EVENT_CALL: ClassVar[OPCODE] = ...
    PATCHPOINT: ClassVar[OPCODE] = ...
    PHI: ClassVar[OPCODE] = ...
    PREALLOCATED_ARG: ClassVar[OPCODE] = ...
    PREALLOCATED_SETUP: ClassVar[OPCODE] = ...
    PSEUDO_PROBE: ClassVar[OPCODE] = ...
    REG_SEQUENCE: ClassVar[OPCODE] = ...
    RET: ClassVar[OPCODE] = ...
    SDIV_ri: ClassVar[OPCODE] = ...
    SDIV_ri_32: ClassVar[OPCODE] = ...
    SDIV_rr: ClassVar[OPCODE] = ...
    SDIV_rr_32: ClassVar[OPCODE] = ...
    SLL_ri: ClassVar[OPCODE] = ...
    SLL_ri_32: ClassVar[OPCODE] = ...
    SLL_rr: ClassVar[OPCODE] = ...
    SLL_rr_32: ClassVar[OPCODE] = ...
    SMOD_ri: ClassVar[OPCODE] = ...
    SMOD_ri_32: ClassVar[OPCODE] = ...
    SMOD_rr: ClassVar[OPCODE] = ...
    SMOD_rr_32: ClassVar[OPCODE] = ...
    SRA_ri: ClassVar[OPCODE] = ...
    SRA_ri_32: ClassVar[OPCODE] = ...
    SRA_rr: ClassVar[OPCODE] = ...
    SRA_rr_32: ClassVar[OPCODE] = ...
    SRL_ri: ClassVar[OPCODE] = ...
    SRL_ri_32: ClassVar[OPCODE] = ...
    SRL_rr: ClassVar[OPCODE] = ...
    SRL_rr_32: ClassVar[OPCODE] = ...
    STACKMAP: ClassVar[OPCODE] = ...
    STATEPOINT: ClassVar[OPCODE] = ...
    STB: ClassVar[OPCODE] = ...
    STB32: ClassVar[OPCODE] = ...
    STB_imm: ClassVar[OPCODE] = ...
    STD: ClassVar[OPCODE] = ...
    STD_imm: ClassVar[OPCODE] = ...
    STH: ClassVar[OPCODE] = ...
    STH32: ClassVar[OPCODE] = ...
    STH_imm: ClassVar[OPCODE] = ...
    STW: ClassVar[OPCODE] = ...
    STW32: ClassVar[OPCODE] = ...
    STW_imm: ClassVar[OPCODE] = ...
    SUBREG_TO_REG: ClassVar[OPCODE] = ...
    SUB_ri: ClassVar[OPCODE] = ...
    SUB_ri_32: ClassVar[OPCODE] = ...
    SUB_rr: ClassVar[OPCODE] = ...
    SUB_rr_32: ClassVar[OPCODE] = ...
    Select: ClassVar[OPCODE] = ...
    Select_32: ClassVar[OPCODE] = ...
    Select_32_64: ClassVar[OPCODE] = ...
    Select_64_32: ClassVar[OPCODE] = ...
    Select_Ri: ClassVar[OPCODE] = ...
    Select_Ri_32: ClassVar[OPCODE] = ...
    Select_Ri_32_64: ClassVar[OPCODE] = ...
    Select_Ri_64_32: ClassVar[OPCODE] = ...
    XADDD: ClassVar[OPCODE] = ...
    XADDW: ClassVar[OPCODE] = ...
    XADDW32: ClassVar[OPCODE] = ...
    XANDD: ClassVar[OPCODE] = ...
    XANDW32: ClassVar[OPCODE] = ...
    XCHGD: ClassVar[OPCODE] = ...
    XCHGW32: ClassVar[OPCODE] = ...
    XFADDD: ClassVar[OPCODE] = ...
    XFADDW32: ClassVar[OPCODE] = ...
    XFANDD: ClassVar[OPCODE] = ...
    XFANDW32: ClassVar[OPCODE] = ...
    XFORD: ClassVar[OPCODE] = ...
    XFORW32: ClassVar[OPCODE] = ...
    XFXORD: ClassVar[OPCODE] = ...
    XFXORW32: ClassVar[OPCODE] = ...
    XORD: ClassVar[OPCODE] = ...
    XORW32: ClassVar[OPCODE] = ...
    XOR_ri: ClassVar[OPCODE] = ...
    XOR_ri_32: ClassVar[OPCODE] = ...
    XOR_rr: ClassVar[OPCODE] = ...
    XOR_rr_32: ClassVar[OPCODE] = ...
    XXORD: ClassVar[OPCODE] = ...
    XXORW32: ClassVar[OPCODE] = ...
    __name__: str
    def __init__(self, *args, **kwargs) -> None: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> Any: ...
    def __int__(self) -> int: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

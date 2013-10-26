import visa
import instruments

class Stanford830(Instrument):
    
    #Initialization
    
    def __init__(self,name,address):
        try:
            self._inst=visa.instrument(address)
        except:
            print "ERROR! Failed to initialize VISA instrument"
            self._inst=None
        if not(self._inst==None):
            self._address=address
        
        #logging.info(__name__ + ' : Initializing instrument')
        Instrument.__init__(self, name, address)
        self.status='Ready'
        
    ############## Constants ##############
    _address = None
    _inst = None

    ############## Functions ##############    
    def convert(self,val,type):
        if type=='float':
            y=float(val)
        if type=='int':
            y=int(val)
        if type=='string':
            y=str(val)
        return y 
        
    def ask(self,command):
        return self._inst.ask(command) 
        
    def write(self,command):
        return self._inst.send(command) 
        

            
    ############## Command: phase ##############    
    '''
    The PHAS command sets or queries the reference phase shift. The
    parameter x is the phase (real number of degrees). The PHAS x command
    will set the phase shift to x. The value of x will be rounded to 0.01deg.
    The phase may be programmed from -360.00 lt x lt 729.99 and will be
    wrapped around at +/-180 deg. For example, the PHAS 541.0 command will
    set the phase to -179.00deg (541-360=181=-179). The PHAS? queries the
    phase shift.
    '''
                
    
    def get_phase (self,i):
        commtxt="PHAS? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
                
    def set_phase (self,i):
        commtxt="PHAS "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: ref_source ##############    
    '''
    The FMOD command sets or queries the reference source. The parameter
    i selects internal (i=1) or external (i=0).
    '''
                
    
    def get_ref_source (self):
        commtxt="FMOD? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_ref_source (self,i):
        commtxt="FMOD "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: frequency ##############    
    '''
    The FREQ command sets or queries the reference frequency. The
    FREQ? query command will return the reference frequency (in internal or
    external mode).
    The FREQ f command sets the frequency of the internal oscillator. This
    command is allowed only if the reference source is internal. The parameter
    f is a frequency (real number of Hz). The value of f will be rounded to
    5 digits or 0.0001 Hz, whichever is greater. The value of f is limited to
    0.001 lt f lt 102000. If the harmonic number is greater than 1, then the
    frequency is limited to nxf lt 102 kHz where n is the harmonic number.
    '''
                
    
    def get_frequency (self):
        commtxt="FREQ? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
                
    def set_frequency (self,i):
        commtxt="FREQ "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: ref_trigger ##############    
    '''
    The RSLP command sets or queries the reference trigger when using the
    external reference mode. The parameter i selects sine zero crossing
    (i=0), TTL rising edge (i=1), , or TTL falling edge (i=2). At frequencies
    below 1 Hz, the a TTL reference must be used.
    '''
                
    
    def get_ref_trigger (self):
        commtxt="RSLP? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_ref_trigger (self,i):
        commtxt="RSLP "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: harmonic ##############    
    '''
    The HARM command sets or queries the detection harmonic. This
    parameter is an integer from 1 to 19999. The HARM i command will set
    the lock-in to detect at the ith harmonic of the reference frequency. The
    value of i is limited by ixf lt 102 kHz. If the value of i requires a detection
    frequency greater than 102 kHz, then the harmonic number will be set to
    the largest value of i such that ixf lt 102 kHz.
    '''
                
    
    def get_harmonic (self):
        commtxt="HARM? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_harmonic (self,i):
        commtxt="HARM "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: amplitude ##############    
    '''
    The SLVL command sets or queries the amplitude of the sine output.
    The parameter x is a voltage (real number of Volts). The value of x will
    be rounded to 0.002V. The value of x is limited to 0.004 lt x lt 5.000.
    '''
                
    
    def get_amplitude (self):
        commtxt="SLVL? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
                
    def set_amplitude (self,i):
        commtxt="SLVL "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: input_config ##############    
    '''
    The ISRC command sets or queries the input configuration. The parameter
    i selects A (i=0), A-B (i=1), I (1 MOhm) (i=2) or I (100 MOhm) (i=3).
    Changing the current gain does not change the instrument sensitivity.
    Sensitivities above 10 nA require a current gain of 1 MOhm. Sensitivities
    between 20 nA and 1 uA automatically select the 1 MOhm current gain. At
    sensitivities below 20 nA, changing the sensitivity does not change the
    current gain.
    '''
                
    
    def get_input_config (self):
        commtxt="ISRC? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_input_config (self,i):
        commtxt="ISRC "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: input_ground ##############    
    '''
    The IGND command sets or queries the input shield grounding. The
    parameter i selects Float (i=0) or Ground (i=1).
    '''
                
    
    def get_input_ground (self):
        commtxt="IGND? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_input_ground (self,i):
        commtxt="IGND "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: input_coupling ##############    
    '''
    The ICPL command sets or queries the input coupling. The parameter i
    selects AC (i=0) or DC (i=1).
    '''
                
    
    def get_input_coupling (self):
        commtxt="ICPL? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_input_coupling (self,i):
        commtxt="ICPL "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: line_notch_filters ##############    
    '''
    The ILIN command sets or queries the input line notch filter status. The
    parameter i selects Out or no filters (i=0), Line notch in (i=1), 2xLine
    notch in (i=2) or Both notch filters in (i=3).
    '''
                
    
    def get_line_notch_filters (self):
        commtxt="ICPL? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_line_notch_filters (self,i):
        commtxt="ICPL "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: sensitivity ##############    
    '''
    The SENS command sets or queries the sensitivity. The parameter i
    selects a sensitivity below.
    i  | sensitivity | i  | sensitivity
    -------------------------------------
    0  | 2 nV/fA     | 13 | 50 uV/pA
    1  | 5 nV/fA     | 14 | 100 uV/pA
    2  | 10 nV/fA    | 15 | 200 uV/pA
    3  | 20 nV/fA    | 16 | 500 uV/pA
    4  | 50 nV/fA    | 17 | 1 mV/nA
    5  | 100 nV/fA   | 18 | 2 mV/nA
    6  | 200 nV/fA   | 19 | 5 mV/nA
    7  | 500 nV/fA   | 20 | 10 mV/nA
    8  | 1 uV/pA     | 21 | 20 mV/nA
    9  | 2 uV/pA     | 22 | 50 mV/nA
    10 | 5 uV/pA     | 23 | 100 mV/nA
    11 | 10 uV/pA    | 24 | 200 mV/nA
    12 | 20 uV/pA    | 25 | 500 mV/nA
                 | 26 | 1 V/uA
    '''
                
    
    def get_sensitivity (self):
        commtxt="SENS? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_sensitivity (self,i):
        commtxt="SENS "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: reserve_mode ##############    
    '''
    The RMOD command sets or queries the reserve mode. The parameter i
    selects High Reserve (i=0), Normal (i=1) or Low Noise (minimum) (i=2).
    See the description of the [Reserve] key for the actual reserves for each
    sensitivity.
    '''
                
    
    def get_reserve_mode (self):
        commtxt="RMOD? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_reserve_mode (self,i):
        commtxt="RMOD "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: time_constant ##############    
    '''
    The OFLT command sets or queries the time constant. The parameter i
    selects a time constant below.
    i | time constant | i  | time constant
    -----------------------------------------
    0 | 10 us         | 10 | 1 s
    1 | 30 us         | 11 | 3 s
    2 | 100 us        | 12 | 10 s
    3 | 300 us        | 13 | 30 s
    4 | 1 ms          | 14 | 100 s
    5 | 3 ms          | 15 | 300 s
    6 | 10 ms         | 16 | 1 ks
    7 | 30 ms         | 17 | 3 ks
    8 | 100 ms        | 18 | 10 ks
    9 | 300 ms        | 19 | 30 ks

    Time constants greater than 30s may NOT be set if the
    harmonic x ref. frequency (detection frequency) exceeds 200 Hz. Time
    constants shorter than the minimum time constant (based upon the filter
    slope and dynamic reserve) will set the time constant to the minimum
    allowed time constant. See the Gain and TIme Constant operation
    section.
    '''
                
    
    def get_time_constant (self):
        commtxt="OFLT? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_time_constant (self,i):
        commtxt="OFLT "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: low_pass_filter_slope ##############    
    '''
    The OFSL command sets or queries the low pass filter slope. The
    parameter i selects 6 dB/oct (i=0), 12 dB/oct (i=1), 18 dB/oct (i=2) or
    24 dB/oct (i=3).
    '''
                
    
    def get_low_pass_filter_slope (self):
        commtxt="OFSL? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_low_pass_filter_slope (self,i):
        commtxt="OFSL "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: sync_filter ##############    
    '''
    The SYNC command sets or queries the synchronous filter status. The
    parameter i selects Off (i=0) or synchronous filtering below 200 Hz (i=1).
    Synchronous filtering is turned on only if the detection frequency (reference
    x harmonic number) is less than 200 Hz.
    '''
                
    
    def get_sync_filter (self):
        commtxt="OFSL? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_sync_filter (self,i):
        commtxt="OFSL "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: display ##############    
    '''
    The DDEF command selects the CH1 and CH2 displays. The parameter
    i selects CH1 (i=1) or CH2 (i=2) and is required. The DDEF i, j, k command
    sets display i to parameter j with ratio k as listed below.
    CH1 (i=1) CH2 (i=2)
    j | display   j | display
    ------------  ------------
    0 | X         0 | Y
    1 | R         1 | q
    2 | X Noise   2 | Y Noise
    3 | Aux In 1  3 | Aux In 3
    4 | Aux In 2  4 | Aux In 4

    k | ratio     k | ratio
    ----------    ----------
    0 | none      0 | none
    1 | Aux In 1  1 | Aux In 3
    2 | Aux In 2  2 | Aux In 4

    The DDEF? i command queries the display and ratio of display i. The
    returned string contains both j and k separated by a comma. For example,
    if the DDEF? 1 command returns "1,0" then the CH1 display is R
    with no ratio.
    '''
                
    
    def get_display (self,i):
        commtxt="DDEF? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_display (self,i,j=0,k=0):
        commtxt="DDEF "
        commtxt=commtxt+str(i)
        if not(j==None):
            commtxt=commtxt","+str(j)
        if not(k==None):
            commtxt=commtxt","+str(k)
        self.write(commtxt)
            
    ############## Command: front_panel_config ##############    
    '''
    The FPOP command sets or queries the front panel (CH1 and CH2)
    output sources. The parameter i selects CH1 (i=1) or CH2 (i=2) and is
    required. The FPOP i, j command sets output i to quantity j where j is
    listed below.

    CH1 (i=1)            |   CH2 (i=2)
                         |
    j | output quantity  |   j | output quantity
    ---------------------------------------------
    0 | CH 1 Display     |   0 | CH 2 Display
    1 | X                |   1 | Y
    '''
                
    
    def get_front_panel_config (self,i):
        commtxt="FPOP? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_front_panel_config (self,i,j):
        commtxt="FPOP "
        commtxt=commtxt+str(i)
        commtxt=commtxt","+str(j)
        self.write(commtxt)
            
    ############## Command: out_offset_expand ##############    
    '''
    The OEXP command sets or queries the output offsets and expands.
    The parameter i selects X (i=1), Y (i=2) or R (i=3) and is required. The
    parameter x is the offset in percent (-105.00 lt x lt 105.00). The parameter
    j selects no expand (j=0), expand by 10 (j=1) or 100 (j=2). The OEXP
    i, x, j command will set the offset and expand for quantity i. This command
    requires BOTH x and j. The OEXP? i command queries the offset
    and expand of quantity i. The returned string contains both the offset and
    expand separated by a comma. For example, if the OEXP? 2 command
    returns "50.00,1" then the Y offset is 50.00% and the Y expand is 10.
    Setting an offset to zero turns the offset off. Querying an offset which is
    off will return 0% for the offset value.
    '''
                
    
    def get_out_offset_expand (self,i):
        commtxt="OEXP? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_out_offset_expand (self,i,x,j=0):
        commtxt="OEXP "
        commtxt=commtxt+str(i)
        commtxt=commtxt","+str(x)
        if not(j==None):
            commtxt=commtxt","+str(j)
        self.write(commtxt)
            
    ############## Command: auto_offset ##############    
    '''
    The AOFF i command automatically offsets X (i=1), Y (i=2) or R (i=3) to
    zero. The parameter i is required. This command is equivalent to pressing
    the [Auto Offset] keys.
    '''
                
    def set_auto_offset (self,i):
        commtxt="AOFF "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: aux_in ##############    
    '''
    The OAUX? command queries the Aux Input values. The parameter i
    selects an Aux Input (1, 2, 3 or 4) and is required. The Aux Input voltages
    are returned as ASCII strings with units of Volts. The resolution is
    1/3 mV. This command is a query only command.
    '''
                
    
    def get_aux_in (self,i):
        commtxt="OAUX? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'')
            
    ############## Command: aux_output ##############    
    '''
    The AUXV command sets or queries the Aux Output voltage when the
    output. The parameter i selects an Aux Output (1, 2, 3 or 4) and is
    required. The parameter x is the output voltage (real number of Volts)
    and is limited to -10.500 lt x lt 10.500. The output voltage will be set to
    the nearest mV.
    '''
                
    
    def get_aux_output (self,i):
        commtxt="AUXV? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_aux_output (self,i,x=0.0):
        commtxt="AUXV "
        commtxt=commtxt+str(i)
        if not(x==None):
            commtxt=commtxt","+str(x)
        self.write(commtxt)
            
    ############## Command: out_interface ##############    
    '''
    The OUTX command sets the output interface to RS232 (i=0) or GPIB
    (i=1). The OUTX i command should be sent before any query commands
    to direct the responses to the interface in use.
    '''
                
    
    def get_out_interface (self):
        commtxt="OUTX? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_out_interface (self,i):
        commtxt="OUTX "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: override_GPIB_remote ##############    
    '''
    In general, every GPIB interface command will put the SR830 into the
    REMOTE state with the front panel deactivated. To defeat this feature,
    use the OVRM 1 command to overide the GPIB remote. In this mode, the
    front panel is not locked out when the unit is in the REMOTE state. The
    OVRM 0 command returns the unit to normal remote operation.
    '''
                
    def set_override_GPIB_remote (self,i):
        commtxt="OVRM "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: key_click ##############    
    '''
    The KCLK command sets or queries the key click On (i=1) or Off (i=0)
    state.
    '''
                
    
    def get_key_click (self):
        commtxt="KCLK? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_key_click (self,i):
        commtxt="KCLK "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: alarm ##############    
    '''
    The ALRM command sets or queries the alarm On (i=1) or Off (i=0)
    state.
    '''
                
    
    def get_alarm (self):
        commtxt="ALRM? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_alarm (self,i):
        commtxt="ALRM "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: store_settings ##############    
    '''
    The SSET i command saves the lock-in setup in setting buffer i (1 lt i lt 9).
    The setting buffers are retained when the power is turned off.
    '''
                
    def set_store_settings (self,i):
        commtxt="SSET "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: recall_settings ##############    
    '''
    The RSET i command recalls the lock-in setup from setting buffer i
    (1 lt i lt 9). Interface parameters are not changed when a setting buffer is
    recalled with the RSET command. If setting i has not been saved prior to
    the RSET i command, then an error will result.
    '''
                
    def set_recall_settings (self,i):
        commtxt="RSET "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: auto_gain ##############    
    '''
    The AGAN command performs the Auto Gain function. This command is
    the same as pressing the [Auto Gain] key. Auto Gain may take some
    time if the time constant is long. AGAN does nothing if the time constant
    is greater than 1 second. Check the command execution in progress bit
    in the Serial Poll Status Byte (bit 1) to determine when the function is
    finished.
    '''
                
    def set_auto_gain (self):
        commtxt="AGAN "
        self.write(commtxt)
            
    ############## Command: auto_reserve ##############    
    '''
    The ARSV command performs the Auto Reserve function. This command
    is the same as pressing the [Auto Reserve] key. Auto Reserve
    may take some time. Check the command execution in progress bit in
    the Serial Poll Status Byte (bit 1) to determine when the function is
    finished.
    '''
                
    def set_auto_reserve (self):
        commtxt="ARSV "
        self.write(commtxt)
            
    ############## Command: auto_phase ##############    
    '''
    The APHS command performs the Auto Phase function. This command
    is the same as pressing the [Auto Phase] key. The outputs will take many
    time constants to reach their new values. Do not send the APHS command
    again without waiting the appropriate amount of time. If the phase
    is unstable, then APHS will do nothing. Query the new value of the phase
    shift to see if APHS changed the phase shift.
    '''
                
    def set_auto_phase (self):
        commtxt="APHS "
        self.write(commtxt)
            
    ############## Command: auto_offset ##############    
    '''
    The AOFF i command automatically offsets X (i=1), Y (i=2) or R (i=3) to
    zero. The parameter i is required. This command is equivalent to pressing
    the [Auto Offset] keys.
    '''
                
    def set_auto_offset (self,i):
        commtxt="AOFF "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: sample_rate ##############    
    '''
    The SRAT command sets or queries the data sample rate. The parameter
    i selects the sample rate listed below.
    i | quantity  |  i  | quantity
    --------------------------------
    0 | 62.5 mHz  |  7  |   8 Hz
    1 | 125 mHz   |  8  |  16 Hz
    2 | 250 mHz   |  9  |  32 Hz
    3 | 500 mHz   |  10 |  64 Hz
    4 | 1 Hz      |  11 | 128 Hz
    5 | 2 Hz      |  12 | 256 Hz
    6 | 4 Hz      |  13 | 512 Hz
    14 | Trigger
    '''
                
    
    def get_sample_rate (self):
        commtxt="SRAT? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_sample_rate (self,i):
        commtxt="SRAT "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: end_of_buffer ##############    
    '''
    The SEND command sets or queries the end of buffer mode. The parameter
    i selects 1 Shot (i=0) or Loop (i=1). If Loop mode is used, make sure
    to pause data storage before reading the data to avoid confusion about
    which point is the most recent.
    '''
                
    
    def get_end_of_buffer (self):
        commtxt="SEND? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_end_of_buffer (self,i):
        commtxt="SEND "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: soft_trigger ##############    
    '''
    The TRIG command is the software trigger command. This command
    has the same effect as a trigger at the rear panel trigger input.
    '''
                
    def set_soft_trigger (self):
        commtxt="TRIG "
        self.write(commtxt)
            
    ############## Command: trigger_start_mode ##############    
    '''
    The SEND command sets or queries the end of buffer mode. The parameter
    i selects 1 Shot (i=0) or Loop (i=1). If Loop mode is used, make sure
    to pause data storage before reading the data to avoid confusion about
    which point is the most recent.
    '''
                
    
    def get_trigger_start_mode (self):
        commtxt="TSTR? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
                
    def set_trigger_start_mode (self,i):
        commtxt="TSTR "
        commtxt=commtxt+str(i)
        self.write(commtxt)
            
    ############## Command: start_data_storage ##############    
    '''
    The STRT command starts or resumes data storage. STRT is ignored if
    storage is already in progress.
    '''
                
    def set_start_data_storage (self):
        commtxt="STRT "
        self.write(commtxt)
            
    ############## Command: pause_data_storage ##############    
    '''
    The PAUS command pauses data storage. If storage is already paused
    or reset then this command is ignored.
    '''
                
    def set_pause_data_storage (self):
        commtxt="PAUS "
        self.write(commtxt)
            
    ############## Command: reset_data_buffer ##############    
    '''
    The REST command resets the data buffers. The REST command can
    be sent at any time - any storage in progress, paused or not, will be
    reset. This command will erase the data buffer.
    '''
                
    def set_reset_data_buffer (self):
        commtxt="REST "
        self.write(commtxt)
            
    ############## Command: read_channel ##############    
    '''
    The OUTP? i command reads the value of X, Y, R or q. The parameter
    i selects X (i=1), Y (i=2), R (i=3) or theta (i=4). Values are returned as ASCII
    floating point numbers with units of Volts or degrees. For example, the
    response might be "-1.01026". This command is a query only command.
    '''
                
    
    def get_read_channel (self,i):
        commtxt="OUTP? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
            
    ############## Command: read_display ##############    
    '''
    The OUTP? i command reads the value of X, Y, R or q. The parameter
    i selects X (i=1), Y (i=2), R (i=3) or theta (i=4). Values are returned as ASCII
    floating point numbers with units of Volts or degrees. For example, the
    response might be "-1.01026". This command is a query only command.
    '''
                
    
    def get_read_display (self,i):
        commtxt="OUTR? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
            
    ############## Command: read_snapshot ##############    
    '''
    The SNAP? command records the values of either 2, 3, 4, 5 or 6 parameters
    at a single instant. For example, SNAP? is a way to query values of
    X and Y (or R and q) which are taken at the same time. This is important
    when the time constant is very short. Using the OUTP? or OUTR? commands
    will result in time delays, which may be greater than the time constant,
    between reading X and Y (or R and q).
    The SNAP? command requires at least two parameters and at most six
    parameters. The parameters i, j, k, l, m, n select the parameters below.

    i,j,k,l,m,n  | parameter
    ------------------------------------
    1            |  X
    2            |  Y
    3            |  R
    4            |  q
    5            |  Aux In 1
    6            |  Aux In 2
    7            |  Aux In 3
    8            |  Aux In 4
    9            |  Reference Frequency
   10            |  CH1 display
   11            |  CH2 display
   
    The requested values are returned in a single string with the values separated
    by commas and in the order in which they were requested. For
    example, the SNAP?1,2,9,5 will return the values of X, Y, Freq and
    Aux In 1. These values will be returned in a single string such as
    "0.951359,0.0253297,1000.00,1.234".
    The first value is X, the second is Y, the third is f, and the fourth is
    Aux In 1.
    The values of X and Y are recorded at a single instant. The values of R
    and q are also recorded at a single instant. Thus reading X,Y OR R,q
    yields a coherent snapshot of the output signal. If X,Y,R and q are all
    read, then the values of X,Y are recorded approximately 10 us apart from
    R,q. Thus, the values of X and Y may not yield the exact values of R and
    q from a single SNAP? query.
    The values of the Aux Inputs may have an uncertainty of up to 32 us. The
    frequency is computed only every other period or 40 ms, whichever is
    longer.
    '''
                
    
    def get_read_snapshot (self,i,j,k=None,l=None,m=None,n=None):
        commtxt="SNAP? "
        commtxt=commtxt+str(i)
        commtxt=commtxt","+str(j)
        if not(k==None):
            commtxt=commtxt+","+str(k)
        if not(l==None):
            commtxt=commtxt+","+str(l)
        if not(m==None):
            commtxt=commtxt+","+str(m)
        if not(n==None):
            commtxt=commtxt+","+str(n)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
            
    ############## Command: read_aux_in ##############    
    '''
    The OAUX? command reads the Aux Input values. The parameter i
    selects an Aux Input (1, 2, 3 or 4) and is required. The Aux Input voltages
    are returned as ASCII strings with units of Volts. The resolution is
    1/3 mV. This command is a query only command.
    '''
                
    
    def get_read_aux_in (self,i):
        commtxt="OAUX? "
        commtxt=commtxt+str(i)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
            
    ############## Command: buffer_points ##############    
    '''
    The SPTS? command queries the number of points stored in the buffer.
    Both displays have the same number of points. If the buffer is reset, then
    0 is returned. Remember, SPTS? returns N where N is the number of
    points - the points are numbered from 0 (oldest) to N-1 (most recent).
    The SPTS? command can be sent at any time, even while storage is in
    progress. This command is a query only command.
    '''
                
    
    def get_buffer_points (self):
        commtxt="SPTS? "
        result=self.ask(commtxt)
        return result #map(self.convert,result,'int')
            
    ############## Command: points_stored_ASCII ##############    
    '''
    The TRCA? command queries the points stored in the Channel i buffer.
    The values are returned as ASCII floating point numbers with the units of
    the trace. Multiple points are separated by commas and the final point is
    followed by a terminator. For example, the response with two points
    might be "-1.234567e-009,+7.654321e-009,".
    The parameter i selects the display buffer (i=1, 2) and is required. Points
    are read from the buffer starting at bin j (j gt 0). A total of k bins are read
    (k gt 1). To read a single point, set k=1. Both j and k are required. If j+k
    exceeds the number of stored points (as returned by the SPTS? query),
    then an error occurs. Remember, SPTS? returns N where N is the total
    number of bins - the TRCA? command numbers the bins from 0 (oldest)
    to N-1 (most recent). If data storage is set to Loop mode, make sure that
    storage is paused before reading any data. This is because the points
    are indexed relative to the most recent point which is continually
    changing.
    '''
                
    
    def get_points_stored_ASCII (self,i,j,k):
        commtxt="TRCA? "
        commtxt=commtxt+str(i)
        commtxt=commtxt","+str(j)
        commtxt=commtxt","+str(k)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')
            
    ############## Command: points_stored_bin ##############    
    '''
    The TRCB? command queries the points stored in the Channel i buffer.
    The values are returned as IEEE format binary floating point numbers
    (with the units of the trace). There are 4 bytes per point. Multiple points
    are not separated by any delimiter. The bytes can be read directly into a
    floating point array (in most languages).
    Do not query the IFC (no command in progress) status bit after sending
    the TRCB command. This bit will not be set until the transfer is complete.
    When using the GPIB interface, EOI is sent with the final byte. The points
    must be read using a binary transfer (see your GPIB interface card software
    manual). Make sure that the software is configured to NOT terminate
    reading upon receipt of a CR or LF.
    When using the RS232 interface, the word length must be 8 bits. The
    points must be read as binary bytes (no checking for linefeeds, carriage
    returns or other control characters). Most serial interface drivers are
    designed for ASCII text only and will not work here. The data transfer does
    not pause between bytes. The receiving interface must always be ready
    to receive the next byte. In general, using binary transfers on the RS232
    interface is not recommended.
    The parameter i selects the display buffer (i=1, 2) and is required. Points
    are read from the buffer starting at bin j (j gt 0). A total of k bins are read
    (k gt 1) for a total transfer of 4k bytes. To read a single point, set k=1. Both
    j and k are required. If j+k exceeds the number of stored points (as
    returned by the SPTS? query), then an error occurs. Remember, SPTS?
    returns N where N is the total number of bins - the TRCB? command
    numbers the bins from 0 (oldest) to N-1 (most recent). If data storage is
    set to Loop mode, make sure that storage is paused before reading any
    data. This is because the points are indexed relative to the most recent
    point which is continually changing.
    '''
                
    
    def get_points_stored_bin (self,i,j,k):
        commtxt="TRCB? "
        commtxt=commtxt+str(i)
        commtxt=commtxt","+str(j)
        commtxt=commtxt","+str(k)
        result=self.ask(commtxt)
        return result #map(self.convert,result,'float')

